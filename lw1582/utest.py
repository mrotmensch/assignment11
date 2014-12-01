import unittest
from Investment import *
from userinput import *

class TestInvestment(unittest.TestCase):
    '''tests if Investment function returns a list'''
    def setUp(self):
        self.position = [1,10,100,1000]

        self.num_trials = 10000
    
    def tearDown(self):
        pass

    def testInvestment(self):
        self.assertEqual(investment(self.position,self.num_trials).shape,(10000,4))

class TestParseInput(unittest.TestCase):
    '''test if user input functions correctly identifies errors and parses input'''

    def setUp(self):
        self.testcase_input_1 = '1,10,$100, 1000'
        self.testcase_input_2 = '-,10000'
        
    def tearDown(self):
        self.testcase_input = None

    def testparseinput(self):
        self.assertEqual(parse_input(self.testcase_input_1,self.testcase_input_2),([1,10,100,1000],10000))


if __name__ == '__main__':
    unittest.main()
