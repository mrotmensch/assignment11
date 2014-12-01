__author__ = 'leilu'
from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from user_defined_exceptions import *


def check_positions(positions_from_user):
    """
    This function will check whether 1000 can be divisible to each elements in the position list
    :param positions_from_user: a list of positions from user
    :return:True if the list is valid and False vice versa
    """
    remainder_list = []  # create a list to store each remainder
    for i in positions_from_user:
        re = 1000 % i
        remainder_list.append(re)

    if sum(remainder_list) == 0:
        return True
    else:
        raise PositionError("Please enter a valid list of positions where 1000 can be divisible to each position. ")



def get_user_number():
    """
    :rtype : get a string from user and convert it to integer
    """
    number = raw_input("Enter a trial number.")
    if number == '':
        get_user_number()
    else:
        try:
            return int(float(number))
        except:
            print "Please enter a valid integer."
            return get_user_number()


def get_user_position():
    """
    :return: get a list of strings from user and convert it to a list of integers
    """
    position_input = raw_input("Enter a list of positions. ").replace(" ", "")

    if position_input == '':
        get_user_position()
    else:

        if position_input[0] != '[' or position_input[-1] != ']':
            raise InputFormatError('Please enter the list of positions in brackets.')
        else:
            try:
                return map(int, position_input[1:-1].split(","))
            except:
                print "Please enter a list of integers as positions, in the format of [ num1, num2, num3,...]"
                return get_user_position()


def investment(positions, num_trails):
    """
    This function will simulate the investment by taking two arguments:
    1)positions: a list of the number of shares
    2)num_trails times: an integer, the number of times that the process will be repeated

    The output return will be a list of lists; each list consists of num_trails elements
    """
    daily_ret = []  # create a list for daily return
    for position in positions:
        position_value = 1000/position
        cumu_ret = []  # create a list for cumulative return
        for trail in range(num_trails):
            cumu_ret.append(position_value*(np.random.choice([0, 2], position, p=[0.49, 0.51]).sum()))
            # specify the return values and their corresponding probability
            # return a list of cumulative return
        daily = [cumu/float(1000) - 1 for cumu in cumu_ret]
        daily_ret.append(daily)

    return daily_ret

