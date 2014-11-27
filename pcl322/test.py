from package.utility import *
from package.exception import *
from package.io import *
import pandas as pd
import unittest
from exceptions import *

class TestIO(unittest.TestCase):
	def setUp(self):
		self.df = pd.DataFrame({"x":[2,3], "y":[100, 200]})
		self.file1 = "/out.txt"
		self.file2 = ""
		self.file3 = "test.txt"

	def test_invalid_file_name(self):
		self.assertRaises(IOError, write_file, self.df, self.file1)
		self.assertRaises(IOError, write_file, self.df, self.file2)

	def test_io_correctly(self):
		self.assertEqual(output_to_file(self.df, self.file3), True)



class TestValidInt(unittest.TestCase):

	def setUp(self):
		self.input1 = "0"
		self.input2 = "-99"
		self.input3 = "123abc456"
		self.input4 = "qqq"
		self.input5 = "0806449+"
		self.input6 = "100"

	def test_zero(self):
		self.assertRaises(IntegerErr, valid_int, self.input1)

	def test_negative(self):
		self.assertRaises(IntegerErr, valid_int, self.input2)

	def test_invalid_format(self):
		self.assertRaises(IntegerErr, valid_int, self.input3)
		self.assertRaises(IntegerErr, valid_int, self.input4)
		self.assertRaises(IntegerErr, valid_int, self.input5)

	def test_correct_format(self):
		self.assertEqual(valid_int(self.input6),True)	


class TestValidPosition(unittest.TestCase):

	def setUp(self):
		self.p1 = "[1,10"
		self.p2 = "1,10,100]"
		self.p3 = "1,10"
		self.p4 = "[1,10,)(]"
		self.p5 = "[1,,10,100]"
		self.p6 = "[1,abc,10]"
		self.p7 = "       [ 1, 10,   100,    1000       ]      "
		self.p8 = "[1,10,100,1000]"

	def test_invalid_format(self):
		self.assertRaises(PositionErr, valid_position, self.p1)
		self.assertRaises(PositionErr, valid_position, self.p2)
		self.assertRaises(PositionErr, valid_position, self.p3)
		self.assertRaises(PositionErr, valid_position, self.p4)
		self.assertRaises(PositionErr, valid_position, self.p5)
		self.assertRaises(PositionErr, valid_position, self.p6)

	def test_space_not_removed(self):
		self.assertRaises(PositionErr, valid_position, self.p7)

	def test_correct_format(self):
		self.assertEqual(valid_position(self.p8), True)



if __name__ == "__main__":
	unittest.main()
