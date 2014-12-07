import unittest
from utility import * 

class testValidPosition(unittest.TestCase):
    '''
    test validPositionInput function in utility.py.
    '''
    def test_positionsBracket(self):
        self.assertFalse(validPositionInput('1,10,100,1000'))
    
    def test_positionsSpace(self):
        self.assertTrue(validPositionInput('[ 1, 10, 100, 1000 ]'))
        
    def test_positionsString(self):
        self.assertFalse(validPositionInput(1234))
    
    def testself_positionsCorrect(self):
        self.assertTrue(validPositionInput('[1,10,100,1000]'))

class testParsePosition(unittest.TestCase):
    '''
    test parsePositionInput function in utility.py.
    '''
    def setUp(self):
        self.testcase = parsePositionInput('[1,10,100,1000]')
    
    def tearDown(self):
        self.string = None
    
    def test_parsePosition(self):
        self.assertEqual(self.testcase, [1,10,100,1000])

if __name__ == '__main__':
    unittest.main()