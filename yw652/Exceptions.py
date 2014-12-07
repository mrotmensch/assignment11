'''
Exception class that defines all possible exceptions
'''

class invalidInputException(Exception):
    '''
    Exception raised when there's invalid input from the user
    '''

    def __str__ (self):
        return "Invalid Input"
    pass

class outputToFileError(Exception):
    '''
    Exception raised when the output file does not exit or bumps into error
    '''

    def __str__(self):
        return "Output file invalid"
    pass