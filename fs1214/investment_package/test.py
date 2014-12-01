'''
Created on 2014.11.30

@author: apple
'''
import unittest
from investment_package.Exceptions import *
from investment_package.Inputfunctions import *

class TestPositionsInput(unittest.TestCase):
    """
    Test whether the input of positions is valid.
    """
    def setUp(self):
        print 'Test the validity of positions input:'
        self.positions = None

    def tearDown(self):
        print 'TestPositionsInput  is over!'


    def test_invalid_positions(self):
        invalid_positions = ['foo','[2,','[f12]','1,10']
        for item in invalid_positions:
            with self.assertRaises(PositionInputException):
                self.positions = ParseList(item)
    
    def test_valid_positions(self):
        valid_positions = ['[12]','[1,10,100]']
        for item in valid_positions:
            self.assertTrue(ParseList(item)) 

class TestNumTrialInput(unittest.TestCase):
    """
    Test whether the input of num_trials is valid.
    """
    def setUp(self):
        print 'Test the validity of num_trials input:'
        self.num_trials = None

    def tearDown(self):
        print 'TestNumTrialInput  is over!'


    def test_invalid_nums(self):
        invalid_nums = ['foo','[2]','-10','10.3']
        for item in invalid_nums:
            with self.assertRaises(NumTrialInputException):
                self.num_trials = ParseNumber(item)
    
    def test_valid_nums(self):
        valid_nums = ['10','10000']
        for item in valid_nums:
            self.assertTrue(ParseNumber(item)) 
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()