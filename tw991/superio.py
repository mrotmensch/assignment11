import sys
import re
from userexception import *
import string


def isvalidInputPosition(input_list):
    """
    Check whether user input valid list of postions
    """
    form = re.compile('^\s*\[\s*\d+\s*,\s*\d+\s*,\s*\d+\s*,\s*\d+\s*\]\s*$')
    match = form.match(input_list)
    if isinstance(input_list, str):
        if match:
            return True
        else:
            return False
    else:
        return False


def isvalidInputTrials(num_trials):
    """Check whether user input valid number of trials
    """
    form = re.compile('^\s*\d+\s*$')
    match = form.match(num_trials)
    if isinstance(num_trials, str):
        if match:
            return True
        else:
            return False
    else:
        return False


def parseInputPosition(position_list):
    """
    return a list of integer position
    if input is not valid, invalidInputPosition will be raised
    """
    if isvalidInputPosition(position_list):
        position_nospace_list = position_list.replace(' ','')
        number_form = re.compile('\d+')
        position = number_form.findall(position_nospace_list)
        position = [int(x) for x in position]
        return position
    else:
        raise invalidInputPosition


def parseInputTrials(num_trials):
    """
    return an integer number of trials
    if input is not valid, invalidInputTrials will be raised
    """
    if isvalidInputTrials(num_trials):
        trials_nospace = num_trials.replace(' ','')
        return int(trials_nospace)
    else:
        raise invalidInputTrials


def superinput():
    """
    return a list of positions and a integer number of trials
    """
    while True:
        try:
            inputlist = raw_input("Please input a list of number of shares to buy in parallel:")
            position = parseInputPosition(inputlist)
            break
        except KeyboardInterrupt:
            sys.exit()
        except invalidInputPosition as e:
            print e
    while True:
        try:
            trials = raw_input("Please input the number of trials:")
            num_trials = parseInputTrials(trials)
            break
        except KeyboardInterrupt:
            sys.exit()
        except invalidInputTrials as e:
            print e
    return position, num_trials
