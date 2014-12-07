import matplotlib.pyplot as plt



def generateGraph(daily_ret, num_trials, pos):
    '''Draws a histogram of daily returns for a given number of trials and parallel investments.
    Args:
        daily_ret: list. normalized list of daily returns
        num_trials: int. number of trials for simulaiton
        pos: int. number of parallel investments.

    Returns:
        None. saves plot as pdf
     '''
    plt.figure()
    plt.hist(daily_ret, bins = 100, range = [-1,1])
    plt.title("Histogram of normalized daily returns for %s days \n %s parallel investments per day" %(num_trials,pos) )
    plt.savefig('histogram_%s_pos.pdf' %pos)
    
    return