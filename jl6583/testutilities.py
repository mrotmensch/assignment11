'''
Created on Nov 30, 2014

@author: luchristopher
'''
import unittest
from utilities import *


class Test_ListParser(unittest.TestCase):


    def setUp(self):
        self.testcase_input = ['[1,2,3]','[-1,1]','[a,b]','whatever']

    def tearDown(self):
        self.testcase_input = None


    def test_listParser(self):
        for i in range(len(self.testcase_input)):
            print listParser(self.testcase_input[i])

class Test_NumIdentifier(unittest.TestCase):
    
    def setUp(self):
        self.testcase_input = ['1','-1','a',' 1   ','--']
    
    def tearDown(self):
        self.testcase_input = None
    
    def test_numIdentifier(self):
        for i in range(len(self.testcase_input)):
            print listParser(self.testcase_input[i])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()