
import re
from simulate.exception import *
def num_input():
    '''
    a function to get user input of positions and num_trials, and then we can make them as position
    s and num_trails
    '''
    #when unput is empty, raise exception
    positions = raw_input('list of positions:\n')
    if positions == '':
        raise InputINvaild('no input')
    num_trials = raw_input('number of trials:\n')
    if num_trials== '':
        raise InputINvaild('no input')
    clean = re.compile(r'[^\d,]+')
    
    try:
        '''clean the input and make it just number'''
        positions_clean = clean.sub("",positions)
        '''write positions clean as a position list'''
        positions = map(int,positions_clean.replace(' ','').split(","))
        #clean the trials
        trials_clean = clean.sub("",num_trials)
        # write the num_trials as a singel int
        num_trials = int(trials_clean.replace(' ','').replace(',',''))
    except:
        raise CleanError('check the input again')
    # return 
    return positions,num_trials