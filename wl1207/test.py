import unittest
import numpy as np
from investment_simulation import investmentSimulation
from exception_class import invalidInputException

class test_investment_simulation(unittest.TestCase):
	
	"""
	Test investmentSimulation(position, num_trials) about its received parameter and returned result.
	"""
	
	def setUp(self):
	
		self.position1 = 10
		self.position2 = 'a'
		
		self.num_trials1 = 10000
		self.num_trials2 = 'b'
	
	def tearDown(self):
		pass
		
	def test_investment_simulation(self):
	
		"""Test if function investment_simulation would return a list. """
		
		self.assertIsInstance(investmentSimulation(self.position1,self.num_trials1),list)
	
	def test_invalid_input(self):
	
		"""Test if function would raise exception when receive any parameters in invalid format. """
		
		self.assertRaises(invalidInputException,investmentSimulation,self.position2,self.num_trials1)
		self.assertRaises(invalidInputException,investmentSimulation,self.position1,self.num_trials2)
	
	
if __name__ == '__main__':
	unittest.main()
		