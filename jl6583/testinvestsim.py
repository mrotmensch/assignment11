'''
Created on Nov 30, 2014

@author: luchristopher
'''
import unittest
from investsim import *


class Test_RunSimulation(unittest.TestCase):


    def setUp(self):
        self.testcase_object = BinomialInvestSimulator(1000,100,0.51)


    def tearDown(self):
        self.testcase_object = None


    def test_runSimulation(self):
        print self.testcase_object.runSimulation(10)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()