###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from geometric_shapes.circle import Circle 
from geometric_shapes.square import Square
from geometric_shapes.rectangle import Rectangle
from geometric_shapes.exceptions.trigger_exception import TriggerException

from typing import List

class ShapeFactory:
	@staticmethod
	def create_shape(shape: str, params: List[float]):
		"""Creates a specific GeometricShape object from the given attributes.

		Usage examples:
			ShapeFactory.create_shape("Circle", 4)
			ShapeFactory.create_shape("Rectangle", [3, 5])

		Parameters:
			shape: str Shape to create.
			params: List[float] List of required parameters.
		"""
		
		TriggerException(shape, params)
		
		return globals()[shape](params)
	   
