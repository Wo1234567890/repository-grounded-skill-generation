SKILLSBENCH_GENERAL_FILTER = """You are a software engineering expert. Given a predefined skill extracted from a successful software-engineering trajectory, evaluate whether the skill is suitable for reuse in similar software-engineering tasks.

# Evaluation guidelines

A good skill should satisfy all of the following:

1. Actionable
   - It should provide a concrete procedure, technique, check, transformation, debugging strategy, or implementation pattern.
   - It should be useful for helping an agent perform a software-engineering task.

2. Reusable
   - It should be applicable to other tasks with similar technical conditions.
   - It should not depend on a single repository instance, task ID, absolute file path, temporary value, or one-off identifier.

3. Technically specific
   - Framework, library, language, protocol, build-system, and tool names are allowed and encouraged when they define when the skill applies.
   - Examples include Spring Security, Maven, React, Flink, Scala, BGP, or a particular API pattern.
   - Technical specificity should not be treated as repository specificity.

4. Non-trivial
   - It should contain meaningful engineering knowledge or procedure.
   - A single obvious command, a thin wrapper around another action, or a generic statement such as "fix the error" is not sufficient.

5. Not merely a task restatement
   - It should add reusable procedural or technical guidance rather than simply repeating the task objective.

# Examples

Bad:
"Edit /workspace/project/src/main/java/example/Foo.java and replace the failing line."

Reason: tied to one repository and file.

Bad:
"Fix the build error."

Reason: too generic and not actionable.

Good:
"When migrating from javax-based APIs to Jakarta-based frameworks, identify affected imports and dependencies together, update them consistently, and compile after each migration stage to expose remaining incompatibilities."

Good:
"When debugging a build failure after a dependency upgrade, first inspect the dependency and plugin versions reported by the build tool before changing application source code."

Good:
"For performance regressions in React components, identify unnecessary re-renders by checking changing props, state, and callback identities before introducing memoization."

Only return "good" or "bad". Do not return any other words.
"""
