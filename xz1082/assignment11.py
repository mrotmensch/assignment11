from invest_simulation import *
from user_exceptions import *
from utility import * 
import matplotlib.pyplot as plt
import numpy as np
import sys

def main():
    '''
    the main program simulates a daily investment, writes results in a text file, and plots the returns for each
    position in [1,10,100,1000] in histograms 
    '''
    #take user input for a list of the number of shares to buy and put them into a list
    positions_input = raw_input('a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]? ')
    positions = parsePositionInput(positions_input)  
    #take user input for the number of times to repeat the test
    try:
        num_trials = int(raw_input('how many times to repeat the test?'))
    except ValueError:
        print 'cannot convert string to integer' 

    #open a file to write
    try:
        results = open('results.txt', 'w')
    except IOError:
        print 'I/O error: cannot open a file'
        sys.exit()
        
    for position in positions:
        daily_ret = investment(position, num_trials)
        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        results.write('Position is: '+ str(position) + '\n')
        results.write('Mean: '+ str(mean) + ' Std: '+ str(std) + '\n')
        
        #plot a histogram with x = [-1, 1] and y as the number of trials
        p = plt.figure()
        plt.hist(daily_ret, 100, range = [-1, 1])
        plt.title('Histogram of Daily Return with Position {}'.format(position))
        plt.xlabel('Daily Return')
        p.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))	

    results.close()

if __name__ == '__main__':
    main()
        