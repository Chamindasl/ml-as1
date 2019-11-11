class InvalidFileError(BaseException):
    """
    Raised when file in not in correct format
    """
    pass


class FileNotReadableError(BaseException):
    """
    Raised when file is not readable, File is not exist or no permission to read
    """
    pass
