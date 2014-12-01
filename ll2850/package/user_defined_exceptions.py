__author__ = 'leilu'

from exceptions import *


class PositionError(Exception):
    """
    This exception will raise when 1000 can not be divided by some elements from the list of string that user inputS
    """
    pass


class InputFormatError(Exception):
    """
    This exception will raise  user's input is in the wrong format.
    """
    pass