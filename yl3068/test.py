import unittest
from investment.utility import *

#Test for int_position function
class intPositionTests(unittest.TestCase):
    def test_int_position(self):
        self.assertEqual(int_positions('[1,2,3,4]'),[1,2,3,4])
        self.assertEqual(int_positions('[1,10,100,1000]'),[1,10,100,1000])
        self.assertEqual(int_positions('[100,1000]'),[100,1000])

#Test for isvalid_trails function
class isvalidTrailsTests(unittest.TestCase):
    def test_isvalidTrails(self):
        self.assertEqual(isvalid_trails('10000'),10000)
        self.assertEqual(isvalid_trails('hello'),False)
        self.assertEqual(isvalid_trails('[]'),False)
        self.assertEqual(isvalid_trails('-2000'),False)
        self.assertEqual(isvalid_trails('0'),False)
        self.assertEqual(isvalid_trails('9999'),9999)

#Test for isvalid_positions function
class isvalidPositionsTests(unittest.TestCase):
    def test_isvalidPositions(self):
        self.assertEqual(isvalid_positions('[1,10,100,1000]'),[1,10,100,1000])
        self.assertEqual(isvalid_positions('[9,99,999]'),[9,99,999])
        self.assertEqual(isvalid_positions('1,10,100,1000'),False)
        self.assertEqual(isvalid_positions('[1,10,k,100]'),False)
        self.assertEqual(isvalid_positions('[0,1,10,100]'),False)
        self.assertEqual(isvalid_positions('[-1,1]'),False)

if __name__ == '__main__':
    unittest.main()

