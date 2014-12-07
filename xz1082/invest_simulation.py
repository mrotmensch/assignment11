import numpy as np

def investment(position, num_trials):
    '''
    this function accepts a list of number of shares to buy in parallel and the 
    number of times to randomly repeat the test, simulating the investment and 
    outputing daily returns.
    '''
    #for positions in position:
    daily_ret = []
    position_value = 1000 / position
    for trial in range(num_trials):
        #randomly generate samples from a binomial distribution 1 time with
        #.51 probability of success 
        probability = np.random.binomial(1, .51, position)
        cumu_ret = probability.sum() * 2 * position_value 
        daily_ret.append((cumu_ret/1000.) - 1)
    return daily_ret


