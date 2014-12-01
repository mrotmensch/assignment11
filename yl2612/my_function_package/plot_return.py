import matplotlib.pyplot as plt
from simulation import simulation

def daily_return_hist(positions, num_trials):
    '''Receive a list of positions and a number of trials.
       Plot the return of different position in histogram.
    '''
    for position in positions:
        daily_return = simulation(position, num_trials)#calculate the return of each position
        plt.figure()
        plt.hist(daily_return, 100, range=[-1,1])
        plt.xlim(-1,1)
        plt.xlabel('Daily Return')
        plt.ylabel('Frequency in Number')
        plt.title('Daily Return of Position{}'.format(position))
        plt.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))
        