'''
Created on 2014.11.8

@author: apple
'''

from investment_package.InvestmentClass import *
from investment_package.Inputfunctions import *
from investment_package.Exceptions import *
from investment_package.Plothistogram import *
import matplotlib.pyplot as plt
import numpy as np
import sys

    
def main():
    """
    Parse the user input to positions and number of trials.
    When we have $1000 to invest in several positions from the user input. 
    We can simulate several times according to the user input for each position to get the value of daily return.
    Plot a histogram for each position.
    For each position, calculate the mean and standard deviation, and save them into a txt file.
    """
    positions = GetValidInput('Please enter a list of the number of shares to buy: ',ParseList,PositionInputException)
    num_trials =GetValidInput('Please enter a number of trials to repeat the test: ',ParseNumber,NumTrialInputException)
    total_investment = 1000
    
    try:
        f = open('result.txt','w')           
        for position in positions:
            daily_ret = Investment(total_investment).simulation(position, num_trials)
            
            #plot the histogram
            plothist(daily_ret, position)
           
            mean = np.mean(daily_ret) 
            std = np.std(daily_ret)
            #save the mean and std into result.txt
            f.write('Position: {}\n'.format(position))   
            f.write('    Mean: {}; Std: {}\n'.format(mean,std))       
        f.close()
    except IOError as e:
        print 'IO Error: {}. Check your file to process the next step.'.format(e.strerror)
        sys.exit()
    except:
        print 'Unexpected Error'
        sys.exit()

if __name__ == '__main__':
    main()