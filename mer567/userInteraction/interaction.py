import re
import sys
import fnmatch
import numpy as np

class string_not_compatible(Exception):
    pass
class wrong_denominations(Exception):
    pass


def user_input(prompt,user_end,str_parser):
    """ Function clled to except user input. does not terminate until input is valid
    Args:
        prompt: string. the prompt displayed to the user
        user_end: string. command with which user can end program
        str_parser: function. the function with which to parse and verify input.
    Returns:
        input_parsed: the parsed and checked version of user input
    """

    check = False
    while check == False:
        try:
            user_input = raw_input(prompt)
            input_parsed = str_parser(user_input)
            check = True
        except (wrong_denominations, string_not_compatible) as s:
            print s
        except KeyboardInterrupt as k:
            print " \n You chose to terminate the program ... Goodbye now!"
            sys.exit()

    return input_parsed

def parse_input_positions(user_input):
    """  Function attempts to parse user input. If input cannot be parsed, raises appropriate error.

    Args:
        user_input: string. user input for prompt.
    Returns:
        list of positions to be used in simulations. each entry is list is int.

     """
    input_no_space = user_input.replace( " ", "")

    #check for empyt string
    if input_no_space == "":
        raise string_not_compatible("Please make sure your input follows the example : '[1, 10, 100, 1000]' ")

    #check for proper list notation
    if input_no_space[0] != "[" or input_no_space[-1] != "]":
        
        raise string_not_compatible("Please make sure your input follows the example : '[1, 10, 100, 1000]' ")

    # split up string by expected delim
    split_str = input_no_space[1:-1].split("," )

    #if any element in the list is empty, raise exception
    if not any(split_str):
        raise string_not_compatible("Please make sure your input follows the example : '[1, 10, 100, 1000]' ")

    # check that every entry is an int
    try:
        formatted_input = [int(x) for x in split_str]
    except:
        raise string_not_compatible("Please make sure your input follows the example : '[1, 10, 100, 1000]' ")

    #can only purchase it in $1, $10, $100, and $1000 denominations. 
    money_on_each_stock = 1000.0/np.array(formatted_input)
    for money in money_on_each_stock:
        if (money%1 != 0) or money == 0 :
            raise wrong_denominations("smallest denomination available is $1")

    return formatted_input


def parse_input_number(user_input):
    """  Function attempts to parse user input. If input cannot be parsed, raises appropriate error.

    Args:
        user_input: string. user input for prompt.
    Returns:
         int. the number of trials for which the simulation will run.

     """
    input_no_space = user_input.replace( " ", "")

    # tranform into integer number of trials
    try:
        formatted_number = int(input_no_space)

    except:
        raise string_not_compatible("please enter a valid number of trials. Ex: 5")

    return formatted_number



