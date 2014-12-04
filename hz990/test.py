import unittest
from Tools.True_Positions import *

class True_Positions_Test(unittest.TestCase):
	'''unittest of the function True_Positions

	'''
	def setUp(self):
		self.pos1 = '[1,2,20,    100]'
		self.pos2 = '[]'
		self.pos3 = '[3,67,44,100]'

	def True_Positions_case1(self):
		position_test = True_Positions(self.pos1)
		self.assertEqual(position_test.__repr__(), True)

	def True_Positions_case2(self):
		position_test = True_Positions(self.pos2)
		self.assertEqual(position_test.__repr__(), False)

	def True_Positions_case3(self):
		position_test = True_Positions(self.pos3)
		self.assertEqual(position_test.__repr__(), False)

if __name__ == '__main__':
	unittest.main()