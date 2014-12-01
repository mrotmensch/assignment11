# -*- coding: utf-8 -*-
"""Files generated in this program
"""

__all__=['stats','hist_generator']

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def stats(summary,positions_input):
    """Calculate the mean and std for each position and return the statistics 
       report
    """
    mean=pd.DataFrame(index=['Mean Value'],columns=positions_input)
    std=pd.DataFrame(index=['Standard Deviation'],columns=positions_input) 
    for p in positions_input:
        mean[p]=np.mean(summary.loc[p,:])
        std[p]=np.std(summary.loc[p,:])  
    
    stats_report=pd.concat([mean,std])
        
    return stats_report



def hist_generator(summary,pos):
    """Generate histogram for each position
    """
    ax=plt.figure()  
    plt.hist(summary.loc[pos,:],100,range=[-1,1])  
    ax.savefig('histogram_{}_pos.pdf'.format(str(pos).zfill(4)))
