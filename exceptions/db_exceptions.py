class InvalidData(BaseException):
    """
    Raised when provided data is invalid for db insertion
    """

    def __init__(self, message):
        self.message = message

    pass

