from simulation import simulation
import numpy as np


def store_mean_std(positions,num_trials):
    '''
    store the mean and standard deviation of daily return in a file called results.txt.
    '''

    try:
        results = open('results.txt','w') #open a file to store mean and standard deviation
    except:
        print " Errors! Cannot open the file!"
    
    for position in positions:
        daily_ret = simulation(position, num_trials)
        mean = np.mean(daily_ret)
        std = np.std(daily_ret)
        results.write('Position: ' + str(position) + '\n')
        results.write('Mean: ' + str(mean) + '\n')
        results.write('Standard Deviation: ' + str(std) + '\n')
    results.close()