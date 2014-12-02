import re
from user_exceptions import * 

def validPositionInput(user_input):
    '''
    tests whether the user's input is in a valid list form.
    '''
    if not isinstance(user_input, str):
        return False

    string = user_input.strip(' ')
    if string[0] == '[' and string[-1] == ']':
        positions = string[1:-1].split(',')
        for position in positions:
            if int(position):
                return True
            else:
                return False
    else:
        return False 
        

def parsePositionInput(position_string):
    '''
    parses user input string into a list of positions.
    '''
    if validPositionInput(position_string):
        #find all numbers in the input string
        integer_pattern = re.compile('\d+')
        integers = integer_pattern.findall(position_string)
        position_list = [int(x) for x in integers]
        return position_list
    else:
        raise PositionError