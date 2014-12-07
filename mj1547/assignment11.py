import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from pylab import *
from simulate.investmentsimulate import investment
from simulate.userinput import num_input
#import some important method and package

def assignment11():
    '''
    a module to write a txt file and save position hist pdf
    
    '''
    #positions=raw_input('Can you set the num_trials')
    
    
    #positions=[1,10,100,1000]
    #the position list
    #num_trials=100
    # get the answer from my investment method
    positions,num_trials=num_input()
    results=investment(positions,num_trials)
    result=open("results.txt",'w') 
    for num_position in positions:
        #calculate the mean and std
        mu=str(np.mean(results[num_position]))
        std=str(np.std(results[num_position]))
        # write the txt file with each position and mean and std
        result.write('position:'+str(num_position)+ '\n' 'Mean:'+mu+ 'and Std:'+std+'\n')
        result.flush()
        plt.figure()
        #the  hist plot by the results 
        plt.hist(results[num_position],100,range=[-1,1])    
        #save figure with each num_positions  
        plt.savefig('histogram_{0:0>4}_pos.pdf'.format(num_position))       
    result.close()
    print 'program done!'
if __name__ == '__main__':
    assignment11()