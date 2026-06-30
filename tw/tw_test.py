import datetime
import unittest
from tw import TransitionWarningApp


class TestTransitionWarningApp(unittest.TestCase):
    def test_parse_time(self):
        app = TransitionWarningApp()
        parsed_time = app._parse_time("23:59")
        self.assertIsInstance(parsed_time, datetime.datetime)
        self.assertGreater(parsed_time, datetime.datetime.today())

    # TODO: Test 3-digit time input (e.g., "959" for 9:59 AM),
    #   but first we need to do something about how it gives an error
    #   if the time in 24 hour format has already passed for the day.
    def test_parse_time_no_colon(self):
        app = TransitionWarningApp()
        parsed_time = app._parse_time("2359")
        self.assertIsInstance(parsed_time, datetime.datetime)
        self.assertGreater(parsed_time, datetime.datetime.today())


if __name__ == "__main__":
    unittest.main()
