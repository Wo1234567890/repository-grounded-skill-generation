# Event listener management Evidence

- family: 未分类技能
- skill_id: 8ab7d9c6-0610-506d-b327-c9d8908c0519
- support_count: 2

## Evidence 1

- support_id: 5374090b-41a3-506c-89b3-a30bf7f4f1d2
- relation_type: support
- document: d3-docs.md
- doc_id: 6cdc3f25-9cd8-59fc-987c-27814dbcdcb1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/d3-docs.md
- section: API index ​
- span: 49136:49387
- confidence: 0.85
- quote: ### Handling events ​

- selection.on - add or remove event listeners.
- selection.dispatch - dispatch a custom event.
- d3.pointer - get the pointer’s position of an event.
- d3.pointers - get the pointers’ positions of an event.

### Control flow ​

## Evidence 2

- support_id: 9df09201-466e-5abe-960d-9253a36923ce
- relation_type: support
- document: agentops-docs.txt
- doc_id: e68d8672-d178-51a3-a14e-d77ffc8c80e1
- source_file: /Users/ttal0464/Desktop/skill-generation/anything2skill/corpus_normalized/agentops-docs.txt
- section: Integrations
- span: 10840:11078
- confidence: 0.75
- quote: response = ""
for event in message:
    if event.data.choices[0].finish_reason == "stop":
        print("\n")
        print(response)
        print("\n")
    else:
        response += event.text

agentops.end_session('Success')
```

Async
