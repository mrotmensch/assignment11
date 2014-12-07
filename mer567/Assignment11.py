import pandas as ps
import numpy as np
import sys
import matplotlib.pyplot as plt
from pylab import rcParams
rcParams['figure.figsize'] = 8, 6

from InvestmentSim.Simulation import *
from userInteraction.interaction import *

""" This Program is designed to help a hypothetical investor, who is intertested in investing his money in the stockmarket wisely, choose how to optimally destribute his\her money between investments with identical yield probabilities. The program does so by simulating different user-inputted money-distribution scenarios and graphing their expected payoffs. Using this simulation the user can then invest the money in a more informed manner. """


def main():
    """ uses functions in other modules in order to get user input and run simulation according to user specifications. 

    Args:
        None.
    Returns:
        None.
        
    """  
    
    positions = user_input("Please enter a list of poisitons or type 'quit' : ","quit", parse_input_positions)
    num_trials = user_input("Please enter number of trials to simulate or type 'quit': ","quit", parse_input_number)

    print "positions", positions
    print "number of trials", num_trials

    try:
        investment(positions, num_trials) #from simulation module
        print 'Done!'
    except KeyboardInterrupt as k:
            print " \n You chose to terminate the program ... Goodbye now!"
            sys.exit()
    return

if __name__ == "__main__":

    main()



