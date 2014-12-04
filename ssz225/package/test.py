import unittest
from package.exceptions import *
from package.invest import *

class TestInvest(unittest.TestCase):
    def setUp(self):
        self.positions1 = '[1, 10, 100, 1000]'
        self.positions2 = '(1, 10, 100, 1000]'
        self.positions3 = '[3, 4, 10]'
        self.positions4 = '[hello]'
        
        self.trials1 = '10000'
        self.trials2 = 'hello'
        
    def test_isValidPositionsInput(self):
        #check that correct input is returned correctly as a list of int
        self.assertEqual(isValidPositionsInput(self.positions1), [1,10,100,1000])
        #check that exceptions are raised for incorrect input for positions
        self.assertRaises(InvalidListError, isValidPositionsInput, self.positions2)
        self.assertRaises(InvalidListError, isValidPositionsInput, self.positions3)
        self.assertRaises(InvalidListError, isValidPositionsInput, self.positions4)
        
    def test_checkTrialsValidity(self):
        #check that input is returned correctly as an int
        self.assertEqual(checkTrialsValidity(self.trials1), 10000)
        #check that exceptions are raised for input that is not an int
        self.assertRaises(InvalidTrialsError, checkTrialsValidity, self.trials2)
    
    def test_Invest(self):
        #test that a list (daily_ret) is returned when proper input is given
        positions = isValidPositionsInput(self.positions1)
        for position in positions:
            self.assertIsInstance(invest(position, checkTrialsValidity(self.trials1)), list)

if __name__=='__main__':
    unittest.main()
