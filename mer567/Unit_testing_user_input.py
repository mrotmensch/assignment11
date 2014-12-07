
import unittest
from userInteraction.interaction import *

class TestFunctions(unittest.TestCase):
    """ unittest class for user interaction functions
        methods in class:
        1) setUp()
        2) test_shuffle()
    """

    def setUp(self):
        """
        sets up class attributes for later use.
        """
        self.user_input1 = "[10,100,1000]" #correct input format
        self.user_input2 =  "[]"
        self.user_input3 = "[ ,,10,100]"
        self.user_input4 = "(10,100]"
        self.user_input5 = "[9]"

        self.user_number1 =  "100" #correct input format
        self.user_number2 = " "
        self.user_number3 = "9.0"
        self.user_number4 = "10,100"
        self.user_number5 = "[]"

    def test_parse_input_positions(self):
        """  test the raised errors of initial position string input by user"""
        parse_input_positions(self.user_input1)
        self.assertRaises(string_not_compatible, parse_input_positions, self.user_input2)
        self.assertRaises(string_not_compatible, parse_input_positions, self.user_input3)
        self.assertRaises(string_not_compatible, parse_input_positions,self.user_input4)
        self.assertRaises(wrong_denominations, parse_input_positions,self.user_input5)

    def test_parse_input_number(self):
        """  test the raised errors of initial number of trials string input by user"""
        parse_input_number(self.user_number1)
        self.assertRaises(string_not_compatible, parse_input_number, self.user_number2)
        self.assertRaises(string_not_compatible, parse_input_number, self.user_number3)
        self.assertRaises(string_not_compatible, parse_input_number, self.user_number4)
        self.assertRaises(string_not_compatible, parse_input_number, self.user_number5)
        


if __name__ == '__main__':
    unittest.main()