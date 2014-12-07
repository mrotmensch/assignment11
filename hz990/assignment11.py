import sys
import numpy as np
from Tools.SIM_PLOT import *
from Tools.Exceptions import *
from Tools.Convert_Positions import *
from Tools.Read_Num_Trials import *
from Tools.Read_Positions import *
from Tools.True_Positions import *


def main():
    '''This main function simulates with the position list and number of trials given by user.

    Step 1. Checking the format of the position list 
    Step 2. Checking the format of the number of trials
    Step 3. Transforming the legal inputs into standard formats
    Step 4. Simulating and Plotting related histograms, then save results'''

    # Step 1
    # Prompting user for a list of positions 
    # If input is illegal, exceptions would be raised
    positions_raw = Read_Positions()

    
    # Step 2
    # Prompting user for number of trials 
    # If input is illegal, exceptions would be raised
    num_trials_raw = Read_Num_Trials()

    # Step 3
    # Transforming the legal inputs into standard formats
    print '\nInputs are correct...\n\nTransforming formats...'
    positions = Convert_Positions(positions_raw)
    num_trials = int(num_trials_raw)
    
    # Step 4 
    # Simulating & Plotting
    SIM_PLOT(positions, num_trials)

    print '\nSimulations and histograms done.\n'


if __name__ == '__main__':
    main()