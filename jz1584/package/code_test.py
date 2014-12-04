import unittest
from inputCheck import checkList, checkTrail



class Testing(unittest.TestCase):
    """tests for all functions in inputCheck module using the Python unittest module
    """
    def setUp(self):
        pass
    
    def test_checkList(self):
        self.assertEqual(checkList('[1,10,100,1000]'),[1,10,100,1000])
        self.assertRaises(Exception, lambda: checkList('[3sdfsaf]'))
        
    
    def test_checkTrail(self):
        self.assertEqual(checkTrail(499), 499)
        self.assertRaises(ValueError,lambda: checkTrail('sdfs'))

        
if __name__ == '__main__':
    unittest.main()
    