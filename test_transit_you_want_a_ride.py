from unittest import TestCase
from unittest.mock import patch
from transit import you_want_a_ride


class TestYouWantARide(TestCase):
    @patch('builtins.input', return_value='1')
    def test_you_want_a_ride_yes(self, mock_input):
        self.assertEqual(you_want_a_ride(), True)

    @patch('builtins.input', return_value='2')
    def test_you_want_a_ride_no(self, mock_input):
        self.assertEqual(you_want_a_ride(), False)
