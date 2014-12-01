import re
import sys
import os
import scipy as sp
import pandas as pd
import numpy as np

#initialize the position list
def positionInit(position):

    '''
    This function take a string of position in, and return a list of 
    integers
    '''
    positionSplit = position.split(',')
    positionSplit[0] = positionSplit[0].replace('[', '')
    positionSplit[-1] = positionSplit[-1].replace(']', '')

    return [int(i) for i in positionSplit]

#check if the input numbers are integer
def check_input(_input):

    if re.match(r"^\d+$", _input) == None:
        return False
    return True

#check if the position in in the right format
def check_position(_input):

    if re.match(r"^\[(\d+\,)*\d+\]$", _input) == None:
        return False
    return True

#compute the mean and std of the positions
def results_mean_std(position, results):
    '''
    This function takes the position(a list of integers) and simulated
    return of position in, and returns a dataFrame with mean and std
    of each position's return
    '''
    df = pd.DataFrame(index = position, columns = ['mean', 'std'])
    df['mean'] = [np.mean(results[i]) for i in position]
    df['std'] = [np.std(results[i]) for i in position]

    return df
