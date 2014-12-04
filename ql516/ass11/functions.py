# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 13:12:21 2014

@author: LaiQX
"""


import matplotlib.pyplot as plt
import numpy as np
from exception_list import *

def daily_ret(position,num_trials):
    """
    input the position and num_trials, compute the daily return of the investment
    then repeat it "num_trials" times. return the result as a list
    
    """
    ret_list = []     # the list of the result
    for i in range(num_trials):         
        total = 0     # calculate each trial's total return 
        for j in range(position):
            # 0.51 chance to get 1.0 return and 0.49 chance to get -1.0 return
            return_rate = np.random.choice([0,2],p=[0.49,0.51])
            total = total + (1000/position)*return_rate
        total_ret = (total/1000.0) - 1
        ret_list.append(total_ret)
    return ret_list



def verify_positions(position_list):  
    """
    verify the input position list, if it is not valid, raise exception
    return a verified position_list
    """
    try:
        position_list = eval(position_list)
    except:
        raise invalid_positions
    aviliable_position = [1,10,100,1000]    
    for i in range(len(position_list)):
        if not(position_list[i] in aviliable_position):
            raise not_a_valid_position
    return position_list
    

def verify_num_trials(num_trials):
    """
    verify the input number of trials, if it is not valid, raise exception
    return a verified trial number
    """
    try:
        num_trials = int(num_trials)
    except:
        raise invalid_trial_num
    
    if (num_trials<=0) :
        raise invalid_trial_num
        
    return num_trials
        

def hist_plot(result,positions):
    """
    plot the histogram
    """
    print "Ploting........."
    for position in positions:
        plt.figure()
        plt.hist(result[position],bins=100,range=[-1,1])
        plt.xlim(-1,1)
        plt.xlabel('Daily return')
        plt.ylabel('Frequency')
        plt.title('histograms of position %d' % (position))
        file_name = "output/histogram_%04d_pos.pdf" % (position)
        plt.savefig(file_name)
        plt.close()
        
    