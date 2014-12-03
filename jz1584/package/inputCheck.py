import re, sys
def checkList(positions):
    """ returns a list of numbers after if the 'string' positions is a list of number,otherwise raise exceptions
    """
    Non_number_list=re.findall(r'[A-Z a-z ][; :\w+()?=]', positions)#extract the non-number elements into a list if any
    if positions[0] !='[' or positions[-1] != ']':#check if the input positions is a list 
        raise Exception("Invalid Input, program exit: Please try again and input a list only !")
        sys.exit()#exit the program after an error occurs 
    elif  len(Non_number_list)!=0:
        raise Exception ("program exit: The list you inputed should contains numbers only, please try again")
        sys.exit()#exit the program after an error occurs 
    else: 
        positions=re.findall(r'[+-]?\d+', positions)
        positions=[int(i) for i in positions]#convert a string list back to a list of numbers
        return positions
    

def checkTrail(trail):
    """ return integer type of trail if the input trails is a number, otherwise raise exceptions
    """
    
    try:
        int(trail)
    except ValueError:
        raise ValueError(" program exit: Error: The number of trails should be integers only")
        sys.exit()#exit a program after an error occurs 
    return int(trail)

        


