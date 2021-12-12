###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
class UnsupportedShapeException(Exception):
    """Exception raised when shape name is unvalid.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self):
        self.message = "This is unsupported shape."
        super().__init__(self.message)