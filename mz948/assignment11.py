import numpy as np
import matplotlib.pyplot as plt
from investmentSimulation import *
from userexceptions import *
from supportingFunctions import *

def main():

    '''Main program that simulates the expected results of investment and plot
    the histogram of daily return.'''
    
    # establish global variables
    positions_input = raw_input('a list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]')
    positions = parsePositions(positions_input)
 
    num_trials = raw_input('How many times to randomly repeat the test')
    if validNumTrialCheck(num_trials):
        num_trials = int(num_trials)
    else:
        num_trials = raw_input('How many times to randomly repeat the test')
       

    mean = []
    std = []
    results = open('results.txt', 'w') 

    for position in positions:
        print 'Simulating with position = {} ...'.format(position)
        daily_ret = simulation(position, num_trials)
        mean  = np.mean(daily_ret)
        std = np.std(daily_ret)
        results.write('{} mean:{},std:{} \n'.format(position,mean,std))
        p = plt.figure()
        plt.hist(daily_ret, 100, range=[-1,1])
        plt.title('Histogram of Daily Return with position {}'.format(position))
        plt.xlabel('Daily return')
        p.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))

    results.close()

if __name__ == '__main__':
    main()








