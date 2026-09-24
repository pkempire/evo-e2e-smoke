# Evo hosted delivery smoke test

This deliberately small synthetic event-filtering application tests Evo's real
account → cloud VM → code edit → correctness checks → paired measurements → draft
pull request path. It is not a customer workload or a production speedup claim.

Optimize `event_filter.py` while preserving its documented API. The evaluator and
tests are fixed. Run `python3 -m unittest discover -s tests -v` for correctness and
`python3 .fleet/benchmark.py` for the application workload. Only Python's standard
library is required; there are no downloads or environment secrets.

The workload uses deterministic synthetic events. Its independent oracle checks
all retained records and their order. Tests also cover duplicates, Unicode,
input immutability and event identity. Fleet measures complete process wall time,
so setup, data generation and checking overhead are included in reported results.
