class BaseError(Exception):
    """
    Base Error for all other exceptions
    """
    pass


class NotANumber(BaseError):
    """
    Base Error to raise provided data is not a number
    """


class NotANumberList(BaseError):
    """
    Base Error to raise provided data is not a number
    """
