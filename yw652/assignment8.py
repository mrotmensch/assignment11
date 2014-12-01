import matplotlib.pyplot as plt
from simulation import *
from Exceptions import *

def main():
    '''
    Generating input and plotting the graphs for the given positions list, as well as writing statistics
    to the document---'result.txt'.
    '''

    #Take inputs from the users, but the graphs are generated with given position list
    while True:
        try:
            position = raw_input("Please type a list of positions you'd like to invest")
            position = position.strip('[()]').split(',')
            positions = []

            #Raise exception if invalid input appears
            for position in position:
                positions.append(int(position))
            break

        except:
            raise invalidInputException

    while True:

        try:
            num_trial = int(raw_input('Please enter the number of trials'))
            break
        except:
            raise invalidInputException

    return_list = simulation(positions, num_trial)

    #If there's an error with output file
    outputF = open('result1.txt', 'w')

    for i in range(len(return_list)):
        mean = np.mean(return_list[i])
        std = np.std(return_list[i])
        outputF.write("Position is " + str(positions[i]) + '\n')
        outputF.write("The mean of the return is " + str(mean)+ ', ' + "and the standard deviation is " + str(std)+"\n")
        outputF.flush()
    outputF.close()

    #Generating graphs for the given positions
    target = [1,10,100,1000]

    sample = simulation(target,10000)

    for i in range(len(sample)):
        plt.hist(sample[i], 100, range=[-1,1])
        plt.savefig("histogram_" + str(target[i])+ "_pos.pdf")
        plt.close('all')

if __name__ == "__main__":
    main()

