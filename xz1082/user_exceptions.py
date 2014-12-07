class Error(Exception):
    '''
    Base class for exceptions in this module.
    '''
    pass

class InputError(Error):
    '''
    Exception raised for error in user's input.
    '''
    def __str__(self):
        return 'this is not in a valid input form'
    pass

class PositionError(Error):
    '''
    Exception raised for errors in user's input position.
    '''
    def __str__(self):
        return 'this is not in a valid position form'
    pass
