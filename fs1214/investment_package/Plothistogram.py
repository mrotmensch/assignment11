'''
Created on 2014.11.30

@author: apple
'''

import matplotlib.pyplot as plt
import numpy as np

def plothist(daily_ret, position):
    """
    Plot of the result of the trials in the histogram with X axis from -1.0 to +1.0, 
    and Y axis as the number of trials with that result.
    Save each figure into a pdf.
    
    Input:
        daily_ret(float): a list of the daily return from the investment given by an exact position.
        position(int): the number of shares to buy.
    
    """
    plt.figure()
    plt.hist(daily_ret,100,range=[-1.0,1.0])
    plt.xlabel('Daily Return')
    plt.ylabel('The Number of Trials')
    plt.title('Histogram of Daily Return with Position = {}'.format(position))
    plt.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))

