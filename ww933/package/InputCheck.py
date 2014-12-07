__author__ = 'chianti'

from assign8exceptions import *
import re

'''
Positions class is used to check whether the input positions is the desired list of the number of shares to buy
if the input is not a list, raise NotListError
if there is a non-integer element in the input, raise NotIntError
if not all of the integers in the input are positive, raise InvalidPositionError
'''


class Positions():

    def __init__(self, num_of_shares):
        self.shares = num_of_shares

        if type(self.shares) != list:
            raise NotListError('Positions should be a list of the number of shares to buy!')

        for each_position in num_of_shares:
            if type(each_position) != int:
                raise NotIntError('Each position should be an integer! (Since we are assuming that you can purchase an '
                                  'investment instrument in only $1, $10, $100, and $1000 denominations)')

            elif each_position <= 0:
                raise InvalidPositionError('Invalid position! Each position should be position.')

    def __repr__(self):
        return 'Positions(%s)' % self.shares

    def __str__(self):
        return str(self.shares)

'''
Numtrials class is used to check whether the input number of trials is valid.
If the input is not an integer or it is a non-positive integer, raise InvalidNumTrialsError
'''


class NumTrials():

    def __init__(self, num_trials):

        self.num_trials = num_trials

        if type(self.num_trials) != int or self.num_trials <= 0:
            raise InvalidNumTrialsError('Invalid number of trials! It should be a positive integer.')

    def __repr__(self):
        return 'NumTrials(%s)' % self.num_trials

    def __str__(self):
        return str(self.num_trials)


'''
TransPositionsInputToList is used to transform the input positions into a list of integers
It will strip [ or ( or ] or ) or { or } first, then split the input contents by , or ; or whitespace
Then, it will convert the splited contents into integers then return
If it fails to convert the contents into integers,  it will raise an exception: NotIntError
'''


def TransAndCheckPositionsInput(InputContents):

    striped_input = InputContents.strip('[(]){} ,;')
    splited_input = re.split('[,;\s]+', striped_input)

    try:
        # Convert each number into an integer
        # For example: ['1', '-100.6'] would then be[1, -100]
        number_input = map(float, splited_input)
        final_input = map(int, number_input)

    except:
        raise PositionsInputError('Sorry, there are something in the input that I cannot recognise')

    return final_input

