###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from geometric_shapes.exceptions.wrong_param_count_exception import WrongParamCountException
from geometric_shapes.exceptions.unsupported_shape_exception import UnsupportedShapeException
from typing import List

class TriggerException():
    """If any exception is exist, throw error.

    Parameters:
			shape: str Shape name to check.
			params: List[float] List of required parameters to check.
    """

    shape_parameter_numbers = {'Circle':1, 'Rectangle':2, 'Square':1}

    def __init__(self, shape: str, params: List[float]):

        shape_name_list = list(self.shape_parameter_numbers.keys())

        if shape not in shape_name_list:
            raise UnsupportedShapeException
        
        if self.shape_parameter_numbers[shape] != len(params):
            raise WrongParamCountException