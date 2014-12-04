__author__ = 'leilu'
from user_defined_exceptions import *
from simulationandfunctions import *
import unittest
import mock


class TestCheckInput(unittest.TestCase):
    def test_invalid_positions(self):
        bogus = [1, 4, 7, 9]
        self.assertRaises(PositionError, check_positions, bogus)


class TestGetUserInput(unittest.TestCase):
    def test_user_number_input(self):
        with mock.patch('__builtin__.raw_input', return_value='4'):
            self.assertEqual(get_user_number(), 4)

    def test_user_position_input(self):
        with mock.patch('__builtin__.raw_input', return_value='[1,10,100,1000]'):
            self.assertEqual(get_user_position(), [1, 10, 100, 1000])


if __name__ == '__main__':
    unittest.main()