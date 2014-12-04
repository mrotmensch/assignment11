# -*- coding: utf-8 -*-
"""This file is to test the investment_instrument functions, mainly focus 
   on user input testing.
"""

from investment_instrument import *
import unittest

class TestPositionsInput(unittest.TestCase):
     """This class was intended to test user input for positions
        1. Make sure the input is in the correct list form with 
        '[' and ']' included with numbers
        2. Make sure the elements in the list is reasonably number of 
        shares in this game
        3. if accepting empty list, return an error msg and prompt for 
        input again
     """
     def test_positions(self):
         self.assertRaises(AssertionError,input_validation,'(1,10,100,1000)')
         self.assertRaises(AssertionError,input_validation,'[1,10,4,100]')
         self.assertRaises(AssertionError,input_validation,'[]')
         
         
         
         
         
         
         
         
         
         
         
if __name__=='__main__':
  unittest.main()