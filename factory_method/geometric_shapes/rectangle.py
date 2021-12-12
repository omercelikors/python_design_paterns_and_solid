###############################################################################
# WORKING AREA
# THIS IS AN AREA WHERE YOU SHOULD WRITE YOUR CODE AND MAKE CHANGES
###############################################################################
from geometric_shapes.shape_interface import ShapeInterface
from geometric_shapes.polygon_interface import PolygonInterface
from geometric_shapes.geometric_shape import GeometricShape
from typing import List

class Rectangle(ShapeInterface,PolygonInterface,GeometricShape):
    def __init__(self, params: List[float]):
        self.height = params[0]
        self.width = params[1]
        self.name = 'Rectangle'
        self.angles = 4

    def get_area(self):
        return self.height * self.width 

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_angles(self):
        return self.angles