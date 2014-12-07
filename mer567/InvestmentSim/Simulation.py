import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 8, 6

from Read_write.read_write import *
from Graph.graph import *

def investment(positions, num_trials):
    """ Simulates the results of investments in a number (positions) or parallel investments. to determine results, function runs the simulation num_trials of times 
    Args:
        positions: list. A list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]. For each entry in the list, 1000/entry must be an integer to ensure investment with valid denominations ($1, $10, $100, and $1000).

        num_trials: int. How many times to randomly repeat the test
        
    Returns:
    	None.  
    """
    position_value = 1000/np.array(positions)
    daily_mean = np.zeros(len(positions))
    daily_std = np.zeros(len(positions))
    

    #loop over different positions
    for i, pos in enumerate(positions):
        cumu_ret = np.zeros(num_trials)

        # simulate returns for num_trials number of days
        for trial in xrange(num_trials):
            
            flip_results = coinFlip(pos)
            
            investment = position_value[i]
            
            returns = profits(investment, flip_results)
            
            cumu_ret[trial] = returns
        
        # normalize and graph a histogram
        daily_ret = (cumu_ret/1000)-1
        generateGraph(daily_ret, num_trials, pos) #from graph module
        
        #calculate daily statistics
        daily_mean[i] = daily_ret.mean()
        daily_std[i] = daily_ret.std()

        mean = daily_ret.mean()
        std = daily_ret.std()
        
    write_to_file(positions, daily_mean, daily_std, num_trials)    
    
    
    return 

def coinFlip(num_investments):
    """ 
	Flips a random coin biased coin (returns 1 with p = 0.51, 0 otherwise).
    Args:
        num_investments: int. The number of biased coins we are flipping.
        
    Returns:
    	flip_results: list. The result of the num_investments coin flips performed. list includes only 1 and 0.
        
    """  
    coins = np.random.random(num_investments)
    
    #convert results according to baised coin (.51 , .49)
    flip_results = map(lambda x: 1 if x <= 0.51 else 0, coins)
    
    return flip_results

def profits(investment, coin_flips ):
    """ 
	converts the coin flips into actual return on investments.

    Args:
        investment:
        coin_flips:
        
    Returns:
    	returns
    """  
    returns = np.sum(investment*coin_flips*2)
    return returns

