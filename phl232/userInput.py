


def getUserPositions():
    
    positionList = input("Enter Position List (e.g. [1, 10]): ")
    
    return positionList 
    
def checkPositions(positions):
    
    result = False 
    
    # positions must be a list of positive integers
    
    # check if position is a list
    if isinstance(positions, list):
        
        # check if list elements are positive integers
        if all([isinstance(x, int) and x > 0 for x in positions]):

            result = True
            
    if result == False:
        
        raise(invalidInputError)
    
    return result
    
def getNumTrials():
    
    
    numTrials = input("Enter Number of Trials: ")
    
    return numTrials 
    
def checkNumTrials(numTrials):
    
    result = isinstance(numTrials, int) and numTrials > 0 
    
    if result == False:
        
        raise(invalidInputError)
    
    return result
    
class invalidInputError(Exception):
    pass