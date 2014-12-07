
import simulation
import unittest
import numpy as np

class TestSimulation(unittest.TestCase):

    def test_badProb(self):
        
        # simulations returns error given improper pWin    

        self.assertRaises(simulation.invalidSimulationError, simulation.simulateInvestmentPayout,1, 1, 1, 2)

    def test_badDenom(self):

        # simulations returns error given improper denomination

        self.assertRaises(simulation.invalidSimulationError, simulation.simulateInvestmentPayout,'a', 1, 1, 0.5)
                
                
    def test_badShares(self):
        
        # simulations returns error given improper numShares        
        
        self.assertRaises(simulation.invalidSimulationError, simulation.simulateInvestmentPayout,1, -1, 1, 0.5)
                
                
    def test_badTrials(self):
        
        # simulations returns error given improper numTrials
        
        self.assertRaises(simulation.invalidSimulationError, simulation.simulateInvestmentPayout,1, 1, 0, 0.5)
                    
    def test_Simulation(self):

        # simulations returns an array given correct input
        
        payout, initialCapital = simulation.simulateInvestmentPayout(1,5,5,1)        
        
        self.assertTrue(isinstance(payout, np.ndarray))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimulation)
    unittest.TextTestRunner(verbosity=2).run(suite)
        