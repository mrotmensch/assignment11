import numpy as np
from simulation.simulation import *
import matplotlib.pyplot as plt
from simulation.exceptions import *


def main():
    '''
    Main function of the simulation. The positions is [1, 10, 100, 1000] and the number of trials is 10000
    '''
    try:
        positionInput = raw_input("Please input the positions set in such a format: '[1, 10, 100, 1000]' or there will be an exception: ")
    except:
        raise InvalidInput('There is something wrong with your input!')

    try:
        num_trials = input("Please input the number of trials(please just input number):")
    except:
        raise InvalidInput("There is something wrong with your input!")

    positions = parseInputPositions(positionInput)

    # simulate the different investment.
    investResult = simulation(positions, num_trials)

    # plot histogram for different position
    for position in positions:
        plt.figure()
        plt.hist(investResult[position], 100, range=[-1.0, 1.0], color='red')
        plt.xlabel('Daily Ret')
        plt.ylabel('Numbers')
        plt.title("Histogram of position-{}'s daily ret".format(position))
        plt.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))

    # set up a file called 'result.txt' and save the mean and std of different position
    try:
        f = open('result.txt', 'w')
        f.write('position' + '\t' + 'mean' + '\t' + 'std' + '\n')
        for position in positions:
            f.write(str(position) + '\t' + str(np.array(investResult[position]).mean()) + '\t' + str(np.array(investResult[position]).std()) + '\n')
        f.close()
    except:
        print "There is something wrong with opening the file and writing into the file."

    print 'Assignment Done!'


if __name__ == '__main__':
    main()
