from invest.investment import Invest
from invest.userinput import list_input, well_input, med_input
from invest.userexceptions import InputError, ConversionError
import matplotlib.pyplot as plt
import numpy as np

def main():
    """ Main program that simulate through each position and plot the histograms of daily return. """

    # Get position list
    while True:
        try:
            positions = list_input('Please specify the list of positions to simulate (separated by commas): ', int)
            break
        except (InputError, ConversionError) as e:
            print e
            continue

    # Get number of trials input
    while True:
        try:
            ntrials = well_input('Please specify number of trials of the simulation: ', int)
            break
        except (InputError, ConversionError) as e:
            print e
            continue
        
    invest_instrument = Invest(1000)    # Create an instance with total asset 1000
    results = ['position mean std']    # List to store simulation results
    
    for position in positions:
        print 'Simulating with position = {} ...'.format(position)
        daily_ret = invest_instrument.simulate(ntrials, position)
        results.append(' '.join(map(str, [position, np.mean(daily_ret), np.std(daily_ret)])))
        
        p = plt.figure()
        # Uncomment if you like xkcd style
        # plt.xkcd()
        plt.hist(daily_ret, 100, range=[-1,1], color='grey')
        plt.title('Histogram of Daily Return with position {}'.format(position))
        plt.xlabel('daily return')
        p.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))

    print 'Saving results ...'
    with open('results.txt', 'w') as f:
        f.write('\n'.join(results))
        

if __name__ == '__main__':
    main()
