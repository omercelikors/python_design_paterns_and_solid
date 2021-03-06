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
from geometric_shapes.square import Square
from geometric_shapes.shape_factory import ShapeFactory
from geometric_shapes.shape_interface import ShapeInterface


class SquareTest(unittest.TestCase):
    def setUp(self):
        self.square = ShapeFactory.create_shape("Square", [3])

    def test_create_square_object(self):
        self.assertIsInstance(self.square, Square)

    def test_square_object_has_correct_name(self):
        self.assertEqual(self.square.get_name(), "Square")

    def test_returns_correct_area(self):
        self.assertEqual(self.square.get_area(), 9)

    def test_return_correct_perimeter(self):
        self.assertEqual(self.square.get_perimeter(), 12)

    def test_returns_correct_angles(self):
        self.assertEqual(self.square.get_angles(), 4)

    def test_implements_geometric_shape(self):
        self.assertIsInstance(self.square, GeometricShape)

    def test_implements_shape_interface(self):
        self.assertIsInstance(self.square, ShapeInterface)

    def test_implements_polygon_interface(self):
        self.assertIsInstance(self.square, PolygonInterface)

    def test_should_throw_wrong_param_count_exception(self):
        with self.assertRaises(WrongParamCountException):
            ShapeFactory.create_shape("Square", [1, 2, 3])

    def test_should_throw_unsupported_shape_exception(self):
        with self.assertRaises(UnsupportedShapeException):
            ShapeFactory.create_shape("Cube", [3])


if __name__ == "__main__":
    unittest.main()
