import matplotlib.pyplot as plt
from simulation import simulate_ret
import numpy as np
import sys


def visualizeRet_to_pdf(positions,num_trails):
    """generate the histograms with X axis from -1.0 to +1.0, Y axis as number of trails with freq results
        and save each histogram of result for each positions into corresponding pdf . 
    """
    for position in positions:
        daily_ret=[]
        #create a list of daily return values for each positions ,which will be used for generating figures.
        dailyRet=simulate_ret(position,num_trails)
        for i in dailyRet: daily_ret.append(dailyRet[i])
        #append each single daily return value into list 
        plt.hist(daily_ret,100,range=[-1.0,1.0])
        plt.ylabel("number of trails")
        plt.xlabel("daily net-return")
        #plt.show()
        if position==1:plt.savefig('histogram_0001_pos.pdf')
        elif position==10:plt.savefig('histogram_0010_pos.pdf')
        elif position==100:plt.savefig('histogram_0100_pos.pdf')
        elif position==1000:plt.savefig('histogram_1000_pos.pdf')
        else: print "error: check position value"
        print 'histogram_%s_pos.pdf generated !'%position # just for testing the progress 
        plt.close()
        

def stat_to_file(positions,num_trails):
    """return a text file ,which contains the results of expected value of daily return 
        and standard deviation of daily return for each position. 
    """
    try:
        result=open("results.txt",'w')
    except:
        print 'not able to open "results.txt" for editing'
        sys.exit()
    
    for position in positions:
        daily_ret=[]
        dailyRet=simulate_ret(position,num_trails)
        for i in dailyRet: daily_ret.append(dailyRet[i])
        ret_array=np.array(daily_ret)
        ret_mean=np.mean(ret_array)
        ret_std=np.std(ret_array)
        result.write('\n\nSome basic statistics of the daily return for  position of %s:\n expected value: %s, standard deviation:%s \n'%(position,ret_mean,ret_std))
    result.close()