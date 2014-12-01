'''
Created on 2014.11.30

@author: apple
'''
import re
from investment_package.Exceptions import *
import sys

def IsValidList(list_input):
    """
    Check whether the input is a valid list containing numbers.
    A valid input must have: '[', several numbers separated by ',', and ']'.
    
    If list_input is valid, return True; otherwise return False.
    Examples:
    '[1,10,100]' : True
    '1,10,100' : False
    'foo': False
    '[1,d,10' : False
    
    """
    if isinstance(list_input, str):
        #Check whether input of list has a valid form
        match = re.search('^\s*\[(\s*\d+\s*,)*\s*\d+\s*\]\s*$',list_input)
        if match:
            return True
        else:
            return False
    else:
        return False

def ParseList(list_input):
    """
    Parse the input of the valid list to a list of numbers.
    
    If list_input is valid, find all the numbers in the input and return a list of numbers(int).
    Otherwise, raise Exception of an input error.
    
    """
    if IsValidList(list_input):
        pattern = re.compile(r'\d+')    
        number_list = pattern.findall(list_input)
        numbers = map(int,number_list) 
        if len(numbers) == 0:
            raise PositionInputException()
        return numbers
    else:
        raise PositionInputException()

def ParseNumber(number_input):
    """
    Check whether the input is a valid number showing how many times to repeat the test.
    A valid input must have be an integer and cannot be negative integer.
    
    If number_input is valid, return the integer; 
    otherwise raise the exception.
    
    """
    
    try:
        intTarget = int(number_input)
    except ValueError:
        raise NumTrialInputException()
    else:
        if intTarget <= 0:
            raise NumTrialInputException()
        else:
            return intTarget

def GetValidInput(command_str,parse_input, exception_input):
    """
    Generate a general function to get a valid result from the user input.
    If the input is invalid, raise the exception.
    The input parameters: 
            command_str: the string of command to guide the user to enter the input
            parse_input: the name of the function that can parse the input
            exception_input: the name of the exception that can raise the corresponding exception.
    Return: 
            result: the valid form of input
    
    Example:
    command_str = 'Please enter a list of the number of shares to buy: '
    positions = GetValidInput(command_str,ParseList,PositionInputException)
    """
    while True:
        input_str = raw_input(command_str)
        if input_str =='quit' or input_str =='exit':
            sys.exit()
        try:
            result = parse_input(input_str)
            return result
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        except (exception_input) as e:
            print e
            continue

