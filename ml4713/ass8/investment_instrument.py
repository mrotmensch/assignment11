# -*- coding: utf-8 -*-
"""Investment Strategy
   Mengfei Li
"""


__all__=['input_validation','single_bet','simulation','strats']

import numpy as np
import pandas as pd



def input_validation(positions):
    """validate the user input for positions as a list and reasonable 
       number of shares to buy that follows the rule
    """
    assert (positions!='[]'), "Empty list. Please try again"
    lbrack,middle,rbrack=positions[0],positions[1:-1],positions[-1]
    numerical_val=middle.split(',')
    assert(lbrack =="[" and rbrack=="]"), "list representation error" 
    num_list=[int(num) for num in numerical_val]
    for elem in num_list:
        assert (elem in [1,10,100,1000]), "{} is not a valid number of shares to buy".format(elem)
    
    return num_list

  
    

def single_bet(pos_val):
    """Imitate a single 'flip' in this gambling problem
    """
    value=np.random.binomial(1,0.51)
    if value==1:
        res=pos_val*2
    else:
        res=0
    
    return res


def simulation(pos):
    """According to different positions, experiment with related trials.
       For example, if we buy 10 shares with $100 for each of shares, then
       we experiment 10 single_bet and store the output as result.
    """
    result=[None]*pos
    pos_val=1000/pos
    for j in np.arange(pos):
        result[j]=single_bet(pos_val)
    return result        
        

def strats(positions,num_trials):
    """Take positions as a list of numer of shares to buy, and num_trials as int
       represents the size of each investment
    """

    cumu_ret=[None]*num_trials
    daily_ret=[None]*num_trials
    summary=pd.DataFrame(index=positions,columns=np.arange(num_trials))
    
    for p in positions:
        for i in np.arange(num_trials):                 
            cumu_ret[i]=sum(simulation(p))            
            daily_ret[i]=(cumu_ret[i]/float(1000))-1   
        summary.loc[p,:]=daily_ret    

    return summary



  
    
    

