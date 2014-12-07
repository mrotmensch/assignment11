__author__ = 'chianti'
import unittest
from InputCheck import *
from assign8exceptions import *

'''
TransAndCheckPositionsInputTests is used to test whether TransAndCheckPositionsInput will check the validity of input
for positions and then transform the input into a list of integers correctly
'''


class TransAndCheckPositionsInputTests(unittest.TestCase):

    def test_invalid_symbol(self):
        with self.assertRaises(PositionsInputError):
            TransAndCheckPositionsInput('900; 200, & ')

    def test_valid_positions1(self):
        self.assertEqual(TransAndCheckPositionsInput('900; 200, 700 20 '), [900, 200, 700, 20])

    def test_valid_positions2(self):
        self.assertEqual(TransAndCheckPositionsInput(' [ 900; 200, 700  20] '), [900, 200, 700, 20])

    def test_valid_positions3(self):
        self.assertEqual(TransAndCheckPositionsInput('  (900; 200, 700  20 ) '), [900, 200, 700, 20])

    def test_valid_positions4(self):
        self.assertEqual(TransAndCheckPositionsInput('  (900; 200, 700.4  20 ) '), [900, 200, 700, 20])

'''
PositionsTests is used to test whether Positions will raise the corresponding exceptions after receiving invalid input
for the positions
'''


class PositionsTests(unittest.TestCase):

    def test_NotListError(self):
        with self.assertRaises(NotListError):
            Positions('900; 200, & ')

    def test_NotIntError(self):
        with self.assertRaises(NotIntError):
            Positions([900, 200, 3.5])

    def test_InvalidPositionError(self):
        with self.assertRaises(InvalidPositionError):
            Positions([200, 300, -20])

'''
NumTrialsTests is used to test whether NumTrials will raise the corresponding exceptions after receiving invalid input
for the number of trials
'''


class NumTrialsTests(unittest.TestCase):

    def test_InvalidNumTrialsError1(self):
        with self.assertRaises(InvalidNumTrialsError):
            NumTrials(-20)

    def test_InvalidNumTrialsError2(self):
        with self.assertRaises(InvalidNumTrialsError):
            NumTrials(20.3)

    def test_InvalidNumTrialsError3(self):
        with self.assertRaises(InvalidNumTrialsError):
            NumTrials('invalid symbol')


if __name__ == '__main__':
    unittest.main()
