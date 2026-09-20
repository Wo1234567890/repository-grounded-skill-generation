# Read Timestamp Extension with Delta Overflow Handling Evidence

- family: 未分类技能
- skill_id: fb580e02-5e97-5a98-9a88-593c837d8917
- support_count: 2

## Evidence 1

- support_id: 5b4c7b6e-7a74-563a-af35-0fbc65be1bc7
- relation_type: support
- document: tictoc-paper.txt
- doc_id: 9fdf1d6f-b6bf-5ce1-8417-e6bbcc7c565c
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/tictoc-paper.txt
- section: 3.2     Protocol Specification
- span: 35321:45111
- confidence: 0.80
- quote: 1632
3.4     Spurious Aborts                                                                 Algorithm 4: Atomically Load Tuple Data and Timestamps
   A transaction may not always be able to validate its read set dur-                    Data: read set entry r, tuple t
ing the validation phase, which leads to aborts that may seem spu-                    1 do
rious. For example, if tuple y in Fig. 1 was originally valid from                    2      v1 = t.read_ts_word()
timestamps 1 to 4, then transaction A’s commit_ts has to be 5. And                    3      read(r.data, t.data)
since x’s rts cannot be extended to 5, A has to abort. In this case,                  4      v2 = t.read_ts_word()
A aborts not because of the timestamps and not data values.                           5 while v1 6= v2 or v1.lock_bit == 1;
   In general, the reason that these aborts occur is because other                    6 r.wts = v1.wts
transactions violate serializability. For the example above, imagine                  7 r.rts = v1.wts + v1.delta
that there exists a transaction C reading tuple x and y after B com-
mits but before A commits. C is able to commit at timestamp 4 as
it observes B’s write to x and the original value of y. C will extend                        TS_word [63]: Lock bit (1 bit).
the rts of y to 4. This means that A cannot commit now without vi-                           TS_word [62:48]: delta = rts − wts (15 bits).
olating serializability because there is a dependency cycle between                          TS_word [47:0]: wts (48 bits).
A, B and C 1 . Note that when A enters the validation phase, it does
not know that C exists or that A would form a dependency cycle                           The highest-order bit is used as the lock bit. wts is stored as a 48-
with other committed transactions.                                                    bit counter. To handle wts overflows, which happens at most once
   Note that in TicToc a transaction aborts only if a tuple it reads                  every several weeks for the most active workloads, the tuples in the
or writes is overwritten by another transaction that enters the vali-                 database are periodically loaded in the background to reset their
dation phase first. So only concurrent transactions (i.e., one starts                 wts. This process is infrequent and can be performed concurrently
before the other commits) can cause aborts. If a transaction com-                     with normal transactions, so its overhead is negligible.
mits, then all transactions that start after it will observe its changes.                Algorithm 4 shows the lock-free implementation of atomically
                                                                                      loading the data and timestamps for the tuple read operation from
3.5     Discussion                                                                    Algorithm 1. TS_word is loaded twice, before and after loading the
                                                                                      data. If these two TS_word instances are the same and both have the
   Beyond scalability and increased concurrency, TicToc’s protocol
                                                                                      lock bit unset, then the data value must not have changed and is still
has two other distinguishing features. Foremost is that the trans-
                                                                                      consistent with the timestamps. Otherwise, the process is repeated
action’s logical commit timestamp order may not agree with the
                                                                                      until both timestamps are consistent. There are no writes to shared
physical commit time order. In the example from shown in Fig. 1,
                                                                                      memory during this process. To avoid starvation, one could revert
transaction A commits physically after transaction B, but its com-
                                                                                      to more heavy-weight latching if this check repeatedly fails.
mit timestamp is less than transaction B’s commit timestamp. This
                                                                                         Similarly, Algorithm 5 shows the steps to atomically extend a
means that A precedes B in the serial schedule. This also indicates
                                                                                      tuple’s rts in TicToc’s validation phase (Algorithm 2). Recall that
that TicToc is not order-preserving serializable, since the serial or-
                                                                                      this operation is called if commit_ts is greater than the local rts;
der may not be the commit order.
                                                                                      the DBMS makes the local version valid at commit_ts by extending
   Another feature of TicToc is that logical timestamps grow more
                                                                                      the rts of the tuple. The first part of the algorithm is the same as
slowly than the number of committed transactions. Moreover, the
                                                                                      explained in Section 3.2.2; validation fails if the tuple’s rts cannot
rate at which the logical timestamp advances is an indicator of the
                                                                                      possibly be extended to commit_ts.
contention level in the workload. This is because different trans-
                                                                                         Since we only encode delta in 15 bits in TS_word, it may over-
actions may commit with the same logical timestamp. Such a sce-
                                                                                      flow if rts and wts grow far apart. If an overflow occurs, we also
nario is possible if two transactions have no conflicts with each
                                                                                      increase wts to keep delta within 15 bits without affecting the cor-
other, or if one transaction reads a version modified by the other
                                                                                      rectness of TicToc. Intuitively, this can be considered a dummy
transaction. At one extreme, if all transactions are read-only and
                                                                                      write to the tuple at the new wts with the same data. Inserting such
thus there is no contention, all transactions will have the same com-
                                                                                      a dummy write does not affect serializability. Increasing wts, how-
mit timestamp. At the other extreme, if all the transactions write
                                                                                      ever, may increase the number of aborts since another transaction
to the same tuple, each commit would increase the tuple’s wts by
                                                                                      may consider the version as being changed while it has not actually
one, and the logical timestamp would increase at the same rate as
                                                                                      changed. This effect is more problematic the fewer bits delta uses.
the number of committed transactions. Since most OLTP work-
                                                                                      Although not shown in the paper, our experiments indicate that 15
loads have some contention, the DBMS’s logical timestamps will
                                                                                      bits is enough for the overflow effect to be negligible.
increase more slowly than the number of committed transactions;
                                                                                         Finally, the new wts and delta are written to a new TS_word
the higher the contention, the faster logical timestamps advance.
                                                                                      and atomically applied to the tuple. The DBMS uses an atomic
We will show this in Section 6.5.
                                                                                      compare-and-swap instruction to make sure that the TS_word has
                                                                                      not been modified by other transactions simultaneously.
3.6     Implementation                                                                   Scanning tuples in a database may miss tuples being inserted
   As shown in Algorithms 1 and 2, both the read and validation                       because they are not observed by the scanning transaction. Stan-
phases require the DBMS to atomically read or write tuples’ times-                    dard techniques for solving this problem include using locks in in-
tamps. But implementing these atomic sections using locks would                       dexes [31] or rescanning the tuples during the validation phase [24].
degrade performance. To avoid this problem, TicToc adopts an op-                      Both techniques incur significant performance overhead. This can
timization from Silo [35] to encode a lock bit and a tuple’s wts and                  be avoided by running the transactions at lower isolation levels

## Evidence 2

- support_id: 5107090a-7b8d-56cc-8820-1b4d93b36dbc
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Debugging Roadmap
- span: 93449:95267
- confidence: 0.75
- quote: # If already instrumented by AgentOps (using our refined check), skip.
    if _is_package_instrumented(package_name):
        logger.debug(f"_should_instrument_package: '{package_name}' already instrumented by AgentOps. Skipping.")
        return False

is_target_agentic = package_name in AGENTIC_LIBRARIES
    is_target_provider = package_name in PROVIDERS

if not is_target_agentic and not is_target_provider:
        logger.debug(
            f"_should_instrument_package: '{package_name}' is not a targeted provider or agentic library. Skipping."
        )
        return False

logger.debug(
        f"_should_instrument_package: Defaulting to False for '{package_name}' (state: _has_agentic_library={_has_agentic_library})"
    )
    return False
