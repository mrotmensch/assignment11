from simulation.simulation import *
from simulation.exceptions import *
import unittest


class parseInputTestCase(unittest.TestCase):
    '''
    test simulation function
    '''
    def setUp(self):
        '''
        set up data used in the test.
        '''
        print 'Test starts!'

        self.positions1 = '[1, 10, 100, 1000   )'
        self.positions2 = ' [1, 10, 100. 1000]  '
        self.positions3 = '(1, 10, 100, 1000]'
        self.positions4 = '[1, 10, 100, 1000 ]  '

    def tearDown(self):
        print 'Test stops!'

    def testInvalidPositions(self):
        with self.assertRaises(InvalidPositions):
            self.position = parseInputPositions(self.positions1)
        with self.assertRaises(InvalidPositions):
            self.position = parseInputPositions(self.positions2)
        with self.assertRaises(InvalidPositions):
            self.position = parseInputPositions(self.positions3)

    def testValidPosition(self):
        self.assertEqual(parseInputPositions(self.positions4), [1, 10, 100, 1000])


if __name__ == '__main__':
    unittest.main()
