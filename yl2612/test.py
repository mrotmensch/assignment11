import unittest
from my_function_package.exceptions import *
from my_function_package.validate_input import *


class TestValidList(unittest.TestCase):
    '''test valid and invalid position'''
    
    def testInvalidListformat(self):
        self.assertRaises(InvalidPosition, get_valid_list, "[1,2[")
        self.assertRaises(InvalidPosition, get_valid_list, "]3,1,9,10[")
        self.assertRaises(InvalidPosition, get_valid_list, "1,10,100,1000")
    
    def testInvalidPositonNumber(self):
        self.assertRaises(InvalidNum, get_valid_list, "[-1,10,1,3,1000]")
        self.assertRaises(InvalidNum, get_valid_list, "[a,2,b,c]")
        self.assertRaises(InvalidNum, get_valid_list, "[3.1,2,7.9]")


    def testValidPosition(self):
        self.assertEqual([1,10,100,1000], get_valid_list('[1, 10, 100, 1000]'))
        self.assertEqual([1,10,2,4], get_valid_list('[1,10,2,4]'))
        self.assertEqual([1,2,2,4], get_valid_list('[1,+2,+2,4]'))




class TestValidNumTrials(unittest.TestCase):
    '''Test valid and invalid number of trials.'''
    
    def testValidNum(self):
        self.assertEqual(10000, get_valid_integer('10000'))
        self.assertEqual(1, get_valid_integer('1'))
        self.assertEqual(1, get_valid_integer('+1'))
    
    def testInvalidNum(self):
        for bogus in ['0', '-1', 'c', '1c', '1+', '[1]']:
            self.assertRaises(InvalidNum, get_valid_integer, bogus)
        
        
if __name__ == "__main__":
    unittest.main()