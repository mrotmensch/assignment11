import numpy as np
import matplotlib.pyplot as plt
from supportingFunctions import *
from simulation import *


def main():
    '''
    This function read number of trials and positions from user, and plot
    the performance of each position
    '''

    while True:
        num_trials = raw_input('Please enter the number of trials')

        if check_input(num_trials) == False:
            print 'Invalid number of trials, please input an integer'
            continue
        break

    while True:
        position = raw_input('Please enter a list of positions').replace(' ', '')

        if check_position(position) == False:
            print 'Invalid positions'
            continue
        break
    
    #get a list of integers of position
    position = positionInit(position)

    #get the daily return of each position
    daily_ret = investment(position, int(num_trials))

    #compute the mean and std of returns of each position
    mean_and_std = results_mean_std(position, daily_ret)

    #write the mean and std into a file called 'results.txt'
    new_file = open('results.txt', 'w')
    new_file.write(mean_and_std.to_string())
    new_file.close()

    #plot the histagram of daily returns of each position
    for i in position:
        plt.hist(daily_ret[i], 100, range = [-1,1])
        plt.savefig('histgram_' + '%04d'%(i) + '_pos.pdf', format = 'pdf')
        plt.close


if __name__ == '__main__':
    main()
