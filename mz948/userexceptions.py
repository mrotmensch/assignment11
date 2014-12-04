class invalidNumTrialException(Exception):
    '''Raise exception when the input string is not a valid position.'''
    def __str__(self):
        return 'Input is not a valid number of trials.'
    pass

class invalidPositionsException(Exception):
    '''Raise exception when at least one of the input positions is not valid.'''
    def __str__(self):
        return 'The list of positions is not in the valid form'
    pass

class negativeNumTrialException(Exception):
    '''Raise exception when the number of trials is smaller or equal to zero.'''
    def __str__(self):
        return 'The number of trials is smaller or equal to zero. The number of trials must be a positive number.'
    pass