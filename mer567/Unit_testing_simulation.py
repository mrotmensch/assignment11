import unittest
from InvestmentSim.Simulation import *

class TestFunctions(unittest.TestCase):
    """ unittest class for user interaction functions
        methods in class:
        1) setUp()
        2) test_simulation()
    """
    def setUp(self):
        """
        sets up class attributes for later use.
        """
        self.positions = [1,10,100,1000]
        self.num_trials = 10000

        self.want_none = investment(self.positions, self.num_trials)
        

    def test_simulation(self): 
        """ method that ensures that the function investment doesn't raise any exceptions and that it doesn't return anything.
        """
        investment(self.positions, self.num_trials)
        self.assertEqual(self.want_none,None)


if __name__ == '__main__':
    unittest.main()