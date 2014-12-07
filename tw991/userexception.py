class invalidInputPosition(Exception):
    """
    Raised when user input invalid position
    """
    def __str__(self):
        return "Input is not valid position!"
    pass


class invalidInputTrials(Exception):
    """
    Raised when user input invalid position
    """
    def __str__(self):
        return "Input is not valid number of trials!"
    pass

