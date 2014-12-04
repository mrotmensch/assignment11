import numpy as np

def simulateInvestmentPayout(denomination, numShares, numTrials, pWin):
    
    '''
    Simulate payout for process defined in HW11
    '''    
    if checkSimulationInput(denomination, numShares, numTrials, pWin):       
        
        
        initialCapital = denomination * numShares
        
        # Array of uniform rv on [0,1]
        randomDraws = np.random.rand(numTrials, numShares)        
    
        # Apply payout rule (profit if # < 0.51, else payout == 0)
        payout = np.zeros([numTrials, numShares])      
        payout[randomDraws <= pWin] = 2 * denomination
        
        return (payout, initialCapital)
        
    else:
        
        print 'Invalid Input'
        raise invalidSimulationError

def calculateDailyRet(payout, initialCapital):

    '''
    calculate simple return
    '''
    
    daily_ret = (payout.sum(1) / (initialCapital))-1
    
    return daily_ret

def checkSimulationInput(denomination, numShares, numTrials, pWin):
    
    denomCheck = isinstance(denomination, (float, int))
    sharesCheck = isinstance(numShares, int) and numShares > 0
    trialsCheck = isinstance(numTrials, int) and numTrials > 0
    probCheck = 0 <= pWin <= 1
    
    return all([denomCheck, sharesCheck, trialsCheck, probCheck])


class invalidSimulationError(Exception):
    pass
