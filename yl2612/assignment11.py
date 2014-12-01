from my_function_package.plot_return import daily_return_hist
from my_function_package.save_mean_std import store_mean_std
from my_function_package.validate_input import *

import sys

def main():
    '''This program stimulates each position, plot the results, store the means and standard deviations in a text file.'''
    try:
        position_input = raw_input('Enter a list of the number of shares to buy in parallel, e.g. [1, 10, 100, 1000]: ')
        positions = get_valid_list(position_input)   #get the validated position in correct format   
    except(KeyboardInterrupt, EOFError):
        sys.exit()
            
    try:
        num_trials_input = raw_input('How many times to randomly repeat the test? ')
        num_trials = get_valid_integer(num_trials_input) #get the validated number of trials2 in correct format   
    except(KeyboardInterrupt, EOFError):
        sys.exit()
            


        
    #plot the return
    print "Saving the plot..."
    daily_return_hist(positions, num_trials)
        
    #store the mean and standard deviation of daily return in a file called results.txt.
    print"Storing the mean and standard deviaiton..."
    store_mean_std(positions, num_trials)
    
    print "Simulation is done! Please check the directory called yl2612 for the plots and results."    

if __name__ == '__main__':
    main()
