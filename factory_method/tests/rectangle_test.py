###############################################################################
# TESTING AREA
# THIS IS AN AREA WHERE YOU CAN TEST YOUR WORK AND WRITE YOUR OWN UNIT TESTS
###############################################################################
import sys
sys.path.append("./")

import unittest

from geometric_shapes.exceptions.wrong_param_count_exception import WrongParamCountException
from geometric_shapes.exceptions.unsupported_shape_exception import UnsupportedShapeException
from geometric_shapes.geometric_shape import GeometricShape
from geometric_shapes.polygon_interface import PolygonInterface
from geometric_shapes.rectangle import Rectangle
from geometric_shapes.shape_factory import ShapeFactory
from geometric_shapes.shape_interface import ShapeInterface


class RectangleTest(unittest.TestCase):
    def setUp(self):
        self.rectangle = ShapeFactory.create_shape("Rectangle", [3, 2])

    def test_create_rectangle_object(self):
        self.assertIsInstance(self.rectangle, Rectangle)

    def test_rectangle_object_has_correct_name(self):
        self.assertEqual(self.rectangle.get_name(), "Rectangle")

    def test_returns_correct_area(self):
        self.assertEqual(self.rectangle.get_area(), 6)

    def test_return_correct_perimeter(self):
        self.assertEqual(self.rectangle.get_perimeter(), 10)

    def test_returns_correct_angles(self):
        self.assertEqual(self.rectangle.get_angles(), 4)

    def test_implements_geometric_shape(self):
        self.assertIsInstance(self.rectangle, GeometricShape)

    def test_implements_shape_interface(self):
        self.assertIsInstance(self.rectangle, ShapeInterface)

    def test_implements_polygon_interface(self):
        self.assertIsInstance(self.rectangle, PolygonInterface)

    def test_should_throw_wrong_param_count_exception(self):
        with self.assertRaises(WrongParamCountException):
            ShapeFactory.create_shape("Rectangle", [])

    def test_should_throw_unsupported_shape_exception(self):
        with self.assertRaises(UnsupportedShapeException):
            ShapeFactory.create_shape("Cube", [3, 2])


if __name__ == "__main__":
    unittest.main()
