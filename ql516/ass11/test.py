# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 13:57:57 2014

@author: LaiQX
"""
from functions import *
from exceptions import *
import unittest

class  test_verify_position(unittest.TestCase):
    def test_out_of_range_1(self):
        self.assertRaises(not_a_valid_position,verify_positions,"[2,10,100]")
    
    def test_out_of_range_2(self):
        self.assertRaises(not_a_valid_position,verify_positions,"[1,10,100,10000]")
        
    def test_out_of_range_3(self):
        self.assertRaises(not_a_valid_position,verify_positions,"[2,14,15]")
    
    def test_invalid_list_1(self):
        self.assertRaises(invalid_positions,verify_positions,"{1,10,100]")
        
    def test_invalid_list_2(self):
        self.assertRaises(invalid_positions,verify_positions,"[bs,10,100]") 
    
    def test_invalid_list_3(self):
        self.assertRaises(invalid_positions,verify_positions,"1,10,100]")
    
    def test_invalid_list_4(self):
        self.assertRaises(invalid_positions,verify_positions,"lajs;f")
    
    def test_valid_positions(self):
        self.assertEqual([100,1,10,1000],verify_positions("[100,1,10,1000]"))


class  test_verify_ntrials(unittest.TestCase):
    def test_invalid_number_1(self):
        self.assertRaises(invalid_trial_num,verify_num_trials,"aldk]")
    
    def test_invalid_number_2(self):
        self.assertRaises(invalid_trial_num,verify_num_trials,"[1,10,100,10000]")
    
    def test_out_of_range(self):
        self.assertRaises(invalid_trial_num,verify_num_trials,"-10")
        
    def test_valid(self):
        self.assertEqual(100,verify_num_trials('100'))
    
class  test_daily_ret(unittest.TestCase):
    def setUp(self):
        np.random.seed(1023123)
        self.position = 10
        self.ntrials = 1000
        self.answer = -0.19999999999999996
    
    def test_daily_return(self):
        self.assertEqual(self.answer,daily_ret(self.position,self.ntrials)[115])
        
        
if __name__ == "__main__":
    unittest.main()