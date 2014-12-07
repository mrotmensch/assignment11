def True_Positions(string):
    '''This function checks whether the position list is legal

    Return True if it is legal
    Return False if not legal'''
    tmp = ''.join(string.split()).strip('[]').split(',')
    positions = [int(i) for i in tmp]
    if positions == []:
        return False
    elif any(i<0 for i in positions): # Position should be positive
        return False
    elif any(1000%i != 0 for i in positions): # Position should be able to divide 1000 in this assignment
        return False
    else:
        return True