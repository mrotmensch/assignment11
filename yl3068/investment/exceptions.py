class Error(Exception):
    pass

class InvalidPositionError(Error):
    """Raise this error when input positions list is invalid"""

    def __init__(self,msg):
        self.msg = msg
        print self.msg
    pass

class InvalidTrailsError(Error):
    """Raise this error when input trails number is invalid"""

    def __init__(self,msg):
        self.msg=msg
        print self.msg
    pass
