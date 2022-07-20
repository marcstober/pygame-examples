import datetime
import unittest
from tw import TransitionWarningApp


class TestTransitionWarningApp(unittest.TestCase):
    def test_parse_time(self):
        app = TransitionWarningApp()
        parsed_time = app._parse_time("23:59")
        self.assertIsInstance(parsed_time, datetime.datetime)
        self.assertGreater(parsed_time, datetime.datetime.today())


if __name__ == "__main__":
    unittest.main()
