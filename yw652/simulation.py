import numpy as np


def simulation(positions, num_trials):
    '''
    Simulate the investment scenarios with given positions and number of trials
    '''

    #Return list that store the return for each of the position
    ret = []

    for position in positions:

        position_value = 1000 / position

        #Cumulative return list that store for each position
        cumu_ret = []
        for n in range(int(num_trials)):
            #For each trial, generate a list of random probability
            probList = []

            #Revenue sum
            sum = 0

            for n in range(position):
                prob = np.random.sample()
                probList.append(prob)

            for prob in probList:
                #prob >= 0.49 represents that there's 51% chance that the investment's about to go double
                sum = sum + position_value * 2 * int(prob >= 0.49)

            cumu_ret.append(sum)

        #Daily return list
        daily_ret = []

        for trial in range(len(cumu_ret)):
            daily_ret.append((cumu_ret[trial]/1000.0) - 1)

        ret.append(daily_ret)

    return ret






