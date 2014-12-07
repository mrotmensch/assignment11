import numpy as np

def investment(position, num_trials):
    '''
    This function take a list of position and the number of trials
    as input, and generate the return performance of each position
    '''
    results = {}
    for i in position:
        position_value = 1000/i
        cumu_ret = []
        for trial in range(num_trials):
            cumu_ret.append(position_value*(np.random.choice([0,2], i, p = [0.49,0.51]).sum()))
        results[i] = np.array(cumu_ret)/1000.0 - 1
    return results

