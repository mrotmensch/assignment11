def Convert_Positions(positions_raw):
    '''This function converts the position list  

    Returns the standard form'''
    
    tmp = ''.join(positions_raw.split()).strip('[]').split(',')
    positions = [int(i) for i in tmp]
    return positions
