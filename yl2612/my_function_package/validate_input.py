from exceptions import *

def get_valid_integer(num):
    '''receive an input, convert to a positive integer '''
    try:
        get_integer = int(num) # try to convert to integer
        
    except:
        raise InvalidNum("Number should be an integer") #raise exception if the input cannot be converted to an integer.
    
    if get_integer <= 0:
        raise InvalidNum("Number should be greater than 0") #raise exception if the input is not a positive integer.
        
    return get_integer


def get_valid_list(position):
    '''receive a list of positions, convert it a correct list format with positive integers in each position.'''
    position_num_list = []
    
    get_position = position.strip()#remove whitespace in the string
    
    
    if get_position[0] =='[' and get_position[-1] == ']': #check it the list has [] format
        
        get_position_num = get_position[1:-1].split(',') #get the positions
        for num in get_position_num:
            position_num = get_valid_integer(num) #get positive integers in each position
            position_num_list.append(position_num)
    else:
        raise InvalidPosition("The list of position should be in [] format")

    return position_num_list