from unittest import TestCase
from unittest.mock import patch
from transit import which_line


class TestWhichLine(TestCase):
    @patch('builtins.input', return_value='1')
    def test_which_line_expo_line(self, mock_input):
        self.assertEqual(which_line({"position": (1, 5)}), "Expo line")

    @patch('builtins.input', return_value='2')
    def test_which_line_canada_line(self, mock_input):
        self.assertEqual(which_line({"position": (1, 5)}), "Canada line")

    @patch('builtins.input', return_value='1')
    def test_which_line_r4_bus_route(self, mock_input):
        self.assertEqual(which_line({"position": (3, 0)}), "R4 Bus Route")

    @patch('builtins.input', return_value='2')
    def test_which_line_99b_line(self, mock_input):
        self.assertEqual(which_line({"position": (3, 0)}), "99B line")

    @patch('builtins.input', return_value='3')
    def test_which_line_seabus(self, mock_input):
        self.assertEqual(which_line({"position": (1, 5)}), "Seabus")
