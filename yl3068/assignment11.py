
import sys
from investment.utility import *
from investment.exceptions import *
import numpy as np
import matplotlib.pyplot as plt

#Define a function to run investment simulation for each position and show the results

def main():

    print "Welcome to the investment simulation system, you get $1000 to invest!"
    
    investment = 1000 #set the initial investment to be 1000
    
    while True:
        try:

            input_positions = raw_input('Please input a list of the number of shares: ')
            positions = isvalid_positions(input_positions)
            if positions == False:
                raise InvalidPositionError('Invalid positions list! \nPlease input a list containing positive integers like [1,10,100,1000]')
                
            break

        except InvalidPositionError:
            pass
        except (KeyboardInterrupt,EOFError):

            print 'Thanks,bye!'
            sys.exit()        
    while True:
        try:

            input_num_trails = raw_input('Please input the number of trails: ')
            num_trails = isvalid_trails(input_num_trails)
            if num_trails == False:
                raise InvalidTrailsError('Invalid trails. Please input a positive integer number like 10000 :)')
            
            break
        except InvalidTrailsError:
            pass
        except (KeyboardInterrupt,EOFError):

            print 'Thanks,bye!'
            sys.exit()

            
    f = open('results/results.txt', 'w') #Open a file to write in mean and standard deviation results

    for position in positions:
        daily_ret = outcome(investment, position, num_trails)
        f.write('\nPosition:{}'.format(position))
        f.write('\nMean:{0}; Std:{1}\n'.format(np.mean(daily_ret), np.std(daily_ret)))
        fig = plt.figure()
        plt.hist(daily_ret, 100, range=[-1,1], color = 'silver', edgecolor = 'DarkGrey')
        plt.title('The histogram of the result for {0} position'.format(position))
        plt.xlabel('daily return')
        fig.savefig('results/histogram_{}_pos.pdf'.format(str(position).zfill(4)))
    f.close()


if __name__ == '__main__':
    main()
