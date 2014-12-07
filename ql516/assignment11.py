# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 19:16:43 2014

@author: LaiQX
"""

import numpy as np
from ass11 import *


def main():
    """
    main function 
    take the given positions and trials
    plot histogram of each position and save the image as pdf format
    calculate the mean and std of each position, save the result in a text file
    """ 
    
    # input the position list and input check
    while 1:
        try:
            positions = raw_input("Please input the position list: (e.g: [10,1,100])\n")
            positions = verify_positions(positions)
            break
        except invalid_positions:
            print "Not a valid positon list, please try again!" 
        except not_a_valid_position:
            print "postion can only be one of [1,10,100,1000], please try again"
    
    # input number of trials and input check
    while 1:
        num_trials = raw_input("please input the trial number:")
        try:
            num_trials = verify_num_trials(num_trials)
            break
        except invalid_trial_num:
            print "not a valid trial number, try again."
    
    # calculate the daily return dict
    print "Calculating......."
    result = {}
    for position in positions:
        result[position] = daily_ret(position,num_trials)
    
    # hist plot
    hist_plot(result,positions)    
    
    # calculate means and stds
    f = open("output/result.txt","a+")   
    for position in positions:
        mean = np.mean(result[position])
        std = np.std(result[position])
        write_string = "position: "+str(position)+"\n"
        f.write(write_string)
        mean_string = "mean: %3.4f" % (mean) + "   std: %5.4f" % (std)+"\n"
        f.write(mean_string)
    f.close()      

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass           
    


