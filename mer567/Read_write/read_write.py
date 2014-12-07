import sys
import pandas as pd

def write_to_file(positions, daily_mean, daily_std, num_trials):
    """ Writes Statistics caluclted to file called results.txt.
    Args:
        positions: list. A list of the number of shares to buy in parallel: e.g. [1, 10, 100, 1000]. For each entry in the list, 1000/entry must be an integer to ensure investment with valid denominations ($1, $10, $100, and $1000).
        daily_mean: list. A list of expected daily returns for each position.
        daily_std: list. A list of the standard deviation for the simulated daily returns for each position.
        num_trials: int. How many times to randomly repeat the test
        
    Returns:
        None.
        creates a file called resutls.txt and writes statistics into it.
    """  
    try: 
        with open('results.txt', 'w') as f:
            for i, pos in enumerate(positions):
                f.write('Statistics for normalized daily returns for %s days \n with %s parallel investments per day \n' %(num_trials,pos))
                f.write("mean: %s \n" %daily_mean[i])
                f.write("standard deviation %s \n" %daily_std[i])
                f.write("\n")
    except IOError as e:
        print "Could not write to file. Please check permissions and try again."

