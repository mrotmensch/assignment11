import numpy as np
from exceptions import *


def simulation(positions, num_trials):
    '''
    Define a simulation function that takes postions and number of trials as inputs and returns the revenue rate of every trial.
    '''

    # use simulationResult to store the final simulation result
    simulationResult = {}

    # for every position in the positions list generate a simulation
    for position in positions:
        simulationResult[position] = []

        for trial in range(num_trials):
            position_value = 1000 / position

            # generate a random number which is in (0, 1) and find whether it is more than 0.49.
            result = np.random.uniform(0, 1, size=position) > 0.49

            daily_ret = (result * position_value * 2).sum() / 1000.0 - 1
            simulationResult[position].append(daily_ret)

    return simulationResult


def parseInputPositions(positionInput):
    '''
    parse the positions the user input and return a list contains these numbers.
    '''

    # delete all the space in the inputs
    positionInput = ''.join(positionInput.split())

    positions = []

    # check whether the user' input is correct.'
    if positionInput[0] != '[' or positionInput[-1] != ']':
        raise InvalidPositions('The positions you input does not fit the criterion that the input requests!')
    else:
        try:
            positionstr = positionInput[1:-1].split(',')
            for item in positionstr:
                positions.append(int(item))
        except:
            raise InvalidPositions("The positions you input are incorrect!")

    return positions
