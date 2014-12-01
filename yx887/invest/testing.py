import unittest
from userinput import med_input, well_input, list_input
from userexceptions import InputError, ConversionError
from investment import Invest

class MedInputTests(unittest.TestCase):
    """ Test med_input function """
    
    def test_exit_flags(self):
        with self.assertRaises(SystemExit):
            med_input(lambda: 'quit')
            
    def test_valid_input(self):
        self.assertEqual(med_input(lambda: '73'), '73')

class WellInputTests(unittest.TestCase):
    """ Test well_input function """
    
    def test_invalid_type_input(self):
        with self.assertRaises(InputError):
            well_input(lambda: '12', 'int')
            
    def test_valid_type_input(self):
        self.assertEqual(type(well_input(lambda: '12', int)), int)
        
    def test_conversion_failure(self):
        with self.assertRaises(ConversionError):
            well_input(lambda: 'hi', int)

class ListInputTests(unittest.TestCase):
    """ Test list_input function """

    def test_invalid_type_input(self):
        with self.assertRaises(InputError):
            list_input(lambda: '11, 12', 'int')

    def test_valid_type_input(self):
        self.assertEqual(list_input(lambda: '11, 12', int), [11, 12])
        self.assertEqual(list_input(lambda: '73', int), [73])
        self.assertEqual(list_input(lambda: '11, 12', str), ['11', '12'])

    def test_conversion_failure(self):
        with self.assertRaises(ConversionError):
            list_input(lambda: '11, hi', int)

if __name__ == '__main__':
    unittest.main()
