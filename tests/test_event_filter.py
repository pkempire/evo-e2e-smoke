import copy
import unittest

from event_filter import select_events


class EventSelection(unittest.TestCase):
    def check(self, events, allowed, expected):
        before_events, before_allowed = copy.deepcopy(events), allowed[:]
        actual = select_events(events, allowed)
        self.assertEqual(actual, expected)
        self.assertEqual(events, before_events)
        self.assertEqual(allowed, before_allowed)
        self.assertEqual(len(actual), len(expected))
        for observed, original in zip(actual, expected):
            self.assertIs(observed, original)

    def test_empty_inputs(self):
        self.check([], ['a'], [])
        self.check([{'user_id': 'a', 'value': 4}], [], [])

    def test_order_duplicates_and_identity(self):
        a = {'user_id': 'a', 'payload': {'score': 3}}
        b = {'user_id': 'b', 'payload': ['untouched']}
        c = {'user_id': 'c', 'payload': None}
        self.check([b, a, b, c, a], ['a', 'b', 'b'], [b, a, b, a])

    def test_strings_are_not_normalized(self):
        events = [{'user_id': value, 'value': index} for index, value in enumerate(['', '0', '00', 'A', 'a', '東京', ' a ', '\0'])]
        self.check(events, ['東京', 'A', '', '\0'], [events[0], events[3], events[5], events[7]])

    def test_varied_sizes_against_independent_linear_oracle(self):
        for count in (1, 2, 31, 513):
            events = [{'user_id': str((index * 17) % 83), 'index': index} for index in range(count)]
            allowed = [str(index) for index in range(0, 83, 3)] + ['0']
            expected = [event for event in events if any(event['user_id'] == value for value in allowed)]
            self.check(events, allowed, expected)


if __name__ == '__main__':
    unittest.main()
