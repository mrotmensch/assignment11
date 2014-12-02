import numpy as np

def simulation(position, num_trials):
    '''
    This is the function that checks the validity of inputs and simulates the 
    investment given the position and number of trials.
    '''
    position_value = 1000 / position
    daily_ret = []
    for trial in range(num_trials):
        #calculate the size of each investment
        
        #probability: 51% win and 49% lose
        return_rate = np.random.choice([0,2],position,p=[0.49,0.51])
        return_rate = return_rate.sum()        
        cumu_ret = return_rate * position_value
        daily_ret.append((cumu_ret / 1000.) - 1)
    return daily_ret 








