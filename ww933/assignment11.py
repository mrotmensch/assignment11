__author__ = 'chianti'

from package.InputCheck import *
from package.GenerateAndOutputReturnFuncs import *
import sys


def main():
    # With positions and num_trials given from the user, this main function
    # shows the result of the investment for each position

    # The first while loop let the user give a list of positions and check its validity
    # I.e : whether it is a list of numbers
    # If not, raise an exception: PositionsInputError
    # Note: if receiving a decimal number, TransAndCheckPositionsInput will automatically convert it into an integer, so
    #       a decimal number will not raise an exception
    while True:
        try:
            raw_positions = raw_input('Give me a list of the number of shares to buy in parallel:')
        except StopIteration or GeneratorExit or KeyboardInterrupt or SystemExit:
            sys.exit()

        try:
            input_positions = TransAndCheckPositionsInput(raw_positions)
            break
        except PositionsInputError:
            print 'Invalid! Need to be a list of numbers.'

    # The second while loop further check the input for positions, if it is not a list of positive numbers, raise
    # the corresponding exceptions
    while True:
        try:
            Positions(input_positions)
            break
        except NotListError or NotIntError or InvalidPositionError:
            print 'Invalid! Need to be a list of positive integers, with format like: [20, 100].'

    # The third while loop let the user give a positive number to indicate how many times to repeat the test
    # and check its validity
    while True:
        try:
            input_num_trials = input('Tell me how many times to randomly repeat the test (give me a positive integer):')
        except StopIteration or GeneratorExit or KeyboardInterrupt or SystemExit:
            sys.exit()

        try:
            NumTrials(input_num_trials)
            break
        except InvalidNumTrialsError:
            print 'Invalid! Need to be a positive integer!'

    # show_return will give us a txt file showing the numerical results for each position containing the mean and std
    # value, as well as some pdf files showing the histogram of the result for each position in the list
    show_return(input_positions, input_num_trials)

if __name__ == '__main__' and True:
    main()
