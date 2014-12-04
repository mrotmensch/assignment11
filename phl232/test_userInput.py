
import userInput
import unittest


class TestUserInput(unittest.TestCase):

    def test_intInputPosition(self):
        
        # error given int input

        self.assertRaises(userInput.invalidInputError, userInput.checkPositions,1)
        
    def test_strInputPosition(self):
        
        # error given string input

        self.assertRaises(userInput.invalidInputError, userInput.checkPositions,'a')
        
    def test_invalidListPosition(self):
        
        # error given list where entries are wrong type

        self.assertRaises(userInput.invalidInputError, userInput.checkPositions,[-1, 1])

    def test_positionOK(self):       
        
        # return true if input is OK
        
        self.assertTrue(userInput.checkPositions([1,10,100,1000]))
        
    def test_strInputTrials(self):
    
        # error given string input

        self.assertRaises(userInput.invalidInputError, userInput.checkNumTrials, 'a')
        
    def test_listInputTrials(self):
    
        # error given list input

        self.assertRaises(userInput.invalidInputError, userInput.checkNumTrials, [1,2])
        
    def test_negInputTrials(self):
    
        # error given negative input

        self.assertRaises(userInput.invalidInputError, userInput.checkNumTrials, -1)
        
    def test_fracInputTrials(self):
    
        # error given fraction input

        self.assertRaises(userInput.invalidInputError, userInput.checkNumTrials, 0.5)
        
    def test_trialsOK(self):       
        
        # return true if input is OK
        
        self.assertTrue(userInput.checkNumTrials(10))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUserInput)
    unittest.TextTestRunner(verbosity=2).run(suite)
        