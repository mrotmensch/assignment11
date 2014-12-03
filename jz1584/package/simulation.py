import numpy as np


def cumu_ret(denomination):
    """ simulates the return (return included the initial value) of one day investment 
        with chosen denomination inputed
    """
    shares=1000/denomination
    #shares indicate numbers of share we can buy  with $1000
    cum=0
    expectRet=[]
    for num_share in range(shares): 
        expect_Prob=np.random.choice([-1,1],p=[.49,.51])
        #specify the probability of two possible returns with corresponding probability
        expected_return= denomination*(1+expect_Prob)# expected_return included original amount of investment
        cum+=expected_return#add up all the returns from different shares
    expectRet.append(cum)#append total return into a list
    return expectRet[0]#return the value of denomination



def simulate_ret(position,num_trials):
    """returns a dictionary of daily return per each dollar invested,
        the daily return will be net return, which is the expected net profit for each dollar invested
    """
    sum_ret={}
    daily_ret={}
    #create a dictionary for daily return with key be the specific single day, 
    #value be the corresponding expected return
    position_value=1000/position
    positionRet=0
    for trial in range(1,num_trials+1):
        positionRet=cumu_ret(position_value)
        sum_ret[trial]=positionRet
        daily_ret[trial]=(sum_ret[trial]/1000.0-1)
        #"Normalize" the return value to be net profit value in each dollar units. 
        #Therefore, the net profit for each dollar invested will be between -1 and 1. 
    return daily_ret



if __name__=='__main__':
    print simulate_ret(1000,10)
    