import unittest
from superio import *
from userexception import *


class TestisvalidInputPosition(unittest.TestCase):
    """
    Test isvalidInputPosition
    """

    def test_space(self):
        self.assertTrue(isvalidInputPosition('[   1,  10, 100, 1000    ]   '))

    def test_number(self):
        self.assertFalse(isvalidInputPosition('[1,10,100]'))

    def test_string(self):
        self.assertFalse(isvalidInputPosition('sdfs'))

    def test_nonstring(self):
        self.assertFalse(isvalidInputPosition(112))

    def test_True(self):
        self.assertTrue(isvalidInputPosition('[1, 10, 100, 1000]'))


class TestisvalidInputTrial(unittest.TestCase):
    """
    Test isvalidInputTrial
    """

    def test_space(self):
        self.assertTrue(isvalidInputTrials('   10  '))

    def test_string(self):
        self.assertFalse(isvalidInputTrials('avsd'))

    def test_nonstring(self):
        self.assertFalse(isvalidInputTrials(123))

    def test_True(self):
        self.assertTrue(isvalidInputTrials('10000'))


class TestparseInputPosition(unittest.TestCase):
    """
    Test parseInputPosition
    """

    def test_True(self):
        self.assertEqual(parseInputPosition(' [ 1 , 10, 100, 1000   ]  '), [1,10,100,1000])

    def test_invalidinput(self):
        with self.assertRaises(invalidInputPosition):
            parseInputPosition('1,10,100,1000')


class TestparseInputTrials(unittest.TestCase):
    """
    Test parseInputTrials
    """

    def test_True(self):
        self.assertEqual(parseInputTrials(' 10000 '), 10000)

    def test_invalidinput(self):
        with self.assertRaises(invalidInputTrials):
            parseInputTrials('[10000]')



if __name__ == '__main__':
    unittest.main()
