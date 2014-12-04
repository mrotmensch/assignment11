
import numpy as np

#This is a function to transfer all elements in the input positions list to be integers
def int_positions(input_positions):
    positions = []
    for i in input_positions[1:-1].split(','):
        positions.append(int(i))
    return positions

#This function is to test if the number of trails inputed by user is valid or not
def isvalid_trails(input_num_trails):
    """
    Attribute:
    input_num_trails: user's input for number of trails, a string
    Return:
    num_trails: if valid, return a int for number of trails
                if invalid, return False
    Examples:
    '10000' >> 10000
    'hello' >> False
    '-2000' >> False

    """

    try:
        num_trails = int(input_num_trails)
        if not num_trails > 0: #number of trails cannot be zero or negtive
            num_trails = False
    except:
        num_trails = False
    return num_trails

#This function is to check if the input list from user is valid or not to be the positions
def isvalid_positions(input_positions):

    """
    Attribute:
    input_positions: list of positions inputed by a user, a string
    Return:
    positions: if valid: list of positions, in which elements are all int
               if invalid: False
    Examples:
    '[1,10,100,1000]' >> [1,10,100,1000]
    '1,10,100,1000' >> False
    '[1,10,k,100]' >> False
    '[0,1,10,100]' >> False
    """

    input_positions = input_positions.replace(' ', '')
    if input_positions[0] == '[' and input_positions[-1] == ']':
        try:
            positions = int_positions(input_positions)
            if not all(position > 0 for position in positions):#position cannot be aero or negtive
                positions = False
        except:
            positions = False
    else:
        positions = False
    return positions

#This is a function to calculate investment outcome for everyday

def outcome(investment, position, num_trails):

    """
    Arguments:
    investment: the total money you invested
    position: number of shares to purchase
    num_trails: number of trails to randomly repeat the test
     
    Returns:
    daily_ret: daily investment outcome rate from this simulation test

    """

    position_value = investment/position
    
    daily_ret = []

    for trail in xrange(num_trails):
        
        #Generate random numbers between 0 to 1 for each position
        outcome = np.random.uniform(low = 0, high = 1, size = position)

        #Calculate the numbers of positions that make revenues 
        revenue_counts = (outcome > 0.49).sum()

        cumu_ret = revenue_counts * position_value * 2
        daily_ret.append((float(cumu_ret)/1000) - 1)
    
    return daily_ret


