import re
from userexceptions import *

    
def validNumTrialCheck(num_trials):
    '''This function tests whether the input of number of trials is a valid 
    integer or not'''
    try:
        num_trials = int(num_trials)
    except:
        raise invalidNumTrialException
    if num_trials <= 0:
        raise negativeNumTrialException
        

    return num_trials

def validPositionsCheck(positions_input):
    '''
    This function parses the input of positions and return the list that 
    contains only integers
    '''
    if not isinstance(positions_input,str):
        return False
    p = re.compile('^\s*\[\d\s*[,\s*\d]*\]\s*$')
    match = p.search(positions_input)
    if match:
        return True
    else:
        return False

def parsePositions(positions_input):
    '''This function takes a string of list of positions as input and returns 
    a list that contains only integers'''
    if validPositionsCheck(positions_input):
        
        positions = positions_input.strip('[ ]').split(',')
        positions = [position for position in positions if position.isdigit()]
        positions = [int(position) for position in positions]
        return positions
    else:
        raise invalidPositionsException


