'''
Created on 2014.11.30

@author: apple
'''

class PositionInputException(Exception):
    """
    Raise when we cannot parse the input of the list to a list of positions.
    """
    def __str__(self):
        return "The input is invalid. A list of the number of shares must have: '[', several numbers separated by ',', and ']' "
    
class NumTrialInputException(Exception):
    """
    Raise when we cannot parse the input of the num_trials to a integer or the integer is negative.
    """
    def __str__(self):
        return "The input is invalid. The number of trials must be a positive integer."
    