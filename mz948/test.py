import unittest
from userexceptions import *
from supportingFunctions import *

class test_valid_positions_check(unittest.TestCase):
    def test_string_with_space(self):
        self.assertTrue(validPositionsCheck('  [4,5]'))
    def test_string_invalid_form(self):
        self.assertFalse(validPositionsCheck('(3,5]'))
    def test_nonstring(self):
        self.assertFalse(validPositionsCheck(3))
    def test_nonlist(self):
        self.assertFalse(validPositionsCheck('erre'))

class test_parse_positions(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parsePositions('[3,10,100   ]'),[3,10,100])
    def test_invalid_input(self):
        with self.assertRaises(invalidPositionsException):
            parsePositions('3,efg')
    def test_single_input(self):
        self.assertEqual(parsePositions('[10000]'),[10000])


class test_num_trials(unittest.TestCase):
    def test_negative(self):
        self.assertRaises(negativeNumTrialException,validNumTrialCheck,'0')            


if __name__ == '__main__':
    unittest.main()