import re
import sys

'''functions take in user input for positions and number of trials, checks input, and converts positons into integers'''

def get_input():

    investment_positions_input = raw_input('Enter a list of positions:\n')
    if investment_positions_input == '':
        raise Exception
    investment_trials_input = raw_input('Enter the number of trials:\n')
    if investment_trials_input == '':
        raise Exception

    return investment_positions_input, investment_trials_input
    
def parse_input(investment_positions_input,investment_trials_input):

    '''define non_decimals as anything that's not a digit or comma'''
    non_decimal = re.compile(r'[^\d,]+')

    try:
        '''clean and parse input'''
        investment_positions_clean = non_decimal.sub("",investment_positions_input)
        investment_positions = map(int, investment_positions_clean.replace(' ','').split(","))
        investment_trials_clean = non_decimal.sub("",investment_trials_input)
        investment_trials = int(investment_trials_clean.replace(' ','').replace(',',''))
    except:
        print "invalid input"

    return investment_positions,investment_trials