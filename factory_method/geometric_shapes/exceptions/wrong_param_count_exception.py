###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
class WrongParamCountException(Exception):
    """Exception raised when param number is unvalid.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "Param count is wrong"
        super().__init__(self.message)
