## Maintaining Evo optimization setup

This repository uses Evo for measured optimization and automated overnight runs.
When code, dependencies, tools, target hardware or entry points change, review
`.evo/optimization.json` and `.evo/fleet.json` in the same pull request. Keep build,
test, workload and diagnostic commands runnable with their declared inputs.
Record required tool versions and target-specific setup in the agreed context.

Preserve the approved objective, correctness requirements and off-limits paths.
Ask the project owner before expanding that agreement or weakening its checks.
Keep benchmark inputs and evaluators identical between baseline and candidate.
After setup changes, execute the unchanged source to establish a new baseline,
then rerun tests and measurements against the exact proposed source and target.
Retain command output, metric units, source identities and hardware identities.
For wall-clock goals, use cycles or CPU clock time for small CPU changes and
synchronized GPU device time for GPU changes when those measurements resolve
the effect. Use them to diagnose, then compare paired elapsed wall-clock time
for the representative complete workload. Record timing boundaries, repetitions
and variation; a local counter win alone is not an end-to-end speedup.
Report actual before/after results; successful tests do not establish formal proof.

Use the approved exploration preference for independent or competing attempts.
Keep experiments isolated, serialize measurements on shared hardware, and test
and measure the combined final changes again before claiming an improvement.
Never put credentials or private runner connection tokens in these files.
