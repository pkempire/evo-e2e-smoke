"""Immutable synthetic API workload; timings come from Fleet, never this code."""
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from event_filter import select_events

allowed = ['user-' + str(index) for index in range(0, 4500, 3)]
events = [{'user_id': 'user-' + str((index * 37) % 4500), 'sequence': index,
           'payload': 'fixed-event-' + str(index % 19)} for index in range(20000)]
expected = [event for index, event in enumerate(events) if ((index * 37) % 4500) % 3 == 0]
for repetition in range(4):
    actual = select_events(events, allowed)
    assert actual == expected, 'Selected event data/order changed'
    assert all(left is right for left, right in zip(actual, expected)), 'Event identity changed'
encoded = json.dumps(actual, sort_keys=True, separators=(',', ':')).encode()
print(json.dumps({'sha256': hashlib.sha256(encoded).hexdigest(), 'selected': len(actual),
                  'input_events': len(events), 'repetitions': 4}, sort_keys=True))
