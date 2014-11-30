class InputError(Exception):
    """ Raised when required_type argument is not a type, this should never be raised in this assignment. """
    pass

class ConversionError(Exception):
    """ Raised when user input cannot be convert to specified type. """
    pass
