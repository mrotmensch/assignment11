from exceptions import *

def get_valid_integer(num):
    '''get the valid integers'''
    try:
        get_integer = int(num)
        
    except:
        raise InvalidNum("Number should be an integer")
    
    if get_integer <= 0:
        raise InvalidNum("Number should be greater than 0")
        
    return get_integer


def get_valid_list(position):
    '''get the valid list of position'''
    position_num_list = []
    
    #remove whitespace in the string    
    get_position = position.strip()
    
    #check it the position has [] format
    if get_position[0] =='[' and get_position[-1] == ']':
        #get the positions
        get_position_num = get_position[1:-1].split(',')
        for num in get_position_num:
            position_num = get_valid_integer(num)
            position_num_list.append(position_num)
    else:
        raise InvalidPosition("The list of position should be in [] format")

    return position_num_list