###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from geometric_shapes.shape_interface import ShapeInterface
from geometric_shapes.geometric_shape import GeometricShape
from typing import List

class Circle(ShapeInterface, GeometricShape):
    def __init__(self, params: List[float]):
        self.radius = params[0]
        self.name = 'Circle'

    def get_area(self):
        return self.PI * self.radius**2

    def get_perimeter(self):
        return 2 * self.PI * self.radius