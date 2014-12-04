import numpy as np
import matplotlib.pyplot as plt


def SIM_PLOT(positions, num_trials):
    '''
    This function simulates the position list with the number of trials given by user.
    Then plots related histograms

    Saves return results in 'results.txt'
    Saves histograms to corresponding pdfs
    
    '''
    print '\nFormats transformed...\n\nLaunching simulations...'
    position_values = np.divide(1000.0, positions)
    Result_return = []        # To store the return data for the final result
    Result_std = []           # To store the Std for the final result
    
    try:
        result = open('results.txt', 'w') # Create a txt file to write related results in
    except:
        raise Open_Error('Cannot open the file, please check.')
    result.write('Position'.ljust(10)+'Mean'.ljust(12)+'Std \n')

    # The following loop Computes the returns and std
    for i in xrange(len(position_values)):
        daily_ret = []
        for j in xrange(num_trials):
            cumu_value = position_values[i] * sum(np.random.choice([0, 2], positions[i], p=[0.49, 0.51]))
            daily_ret.append(cumu_value/1000 - 1)  # computes each daily return
        Result_return.append(np.mean(daily_ret)) 
        Result_std.append(np.std(daily_ret))
        result.write(str(positions[i]).ljust(10)+str(Result_return[i]).ljust(12)+str(Result_std[i]).ljust(12)+'\n')
        
        #Plotting
        plt.figure()
        plt.hist(daily_ret,100, range=[-1,1])
        plt.title('Daily return histogram of position {}'.format(positions[i]))
        plt.xlabel('Daily Return')
        plt.ylabel('Frequency')
        plt.savefig('histogram_'+str(positions[i]).zfill(4)+'_pos.pdf', format='pdf')
    result.close()