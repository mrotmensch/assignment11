__author__ = 'chianti'

'''
PositionsInputError is used in the function TransAndCheckPositionsInput located in InputCheck
if the input contents for positions contain unrecognised values, raise this exception
I.e: if there exist something besides numbers and whitespaces and , ; [ ( ] ) { } , raise this exception
'''


class PositionsInputError(Exception):
    pass


'''
NotListError is used in class positions
if the type of the positions is not a list, raise this exception
'''


class NotListError(Exception):
    pass

'''
NotIntError is used in class positions
if the type of each elements in the list of positions is not an integer, raise this exception
'''


class NotIntError(Exception):
    pass

'''
InvalidPositionError is used in class positions
if all elements in the list of positions are not positive, raise this exception
'''


class InvalidPositionError(Exception):
    pass

'''
InvalidNumTrialsError is used in class NumTrials
if the input is not a valid number suggesting how many times to randomly repeat our test, raise this exception
'''


class InvalidNumTrialsError(Exception):
    pass