#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def testRectangle_valid_arguments(self):
        """
        Test creating an instance of Rectangle with valid arguments.
        """
        r = Rectangle(5, 10, 1, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def testRectangle_invalid_width(self):
        """
        Test creating an instance of Rectangle with invalid width argument.
        """
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 1, 2)

    def testRectangle_invalid_height(self):
        """
        Test creating an instance of Rectangle with invalid height argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 1, 2)

    def testRectangle_invalid_x(self):
        """
        Test creating an instance of Rectangle with invalid x argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 2)

    def testRectangle_invalid_y(self):
        """
        Test creating an instance of Rectangle with invalid y argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 1, "invalid")

    def testRectangle_zero_width(self):
        """
        Test creating an instance of Rectangle with zero width argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 10, 1, 2)

    def testRectangle_zero_height(self):
        """
        Test creating an instance of Rectangle with zero height argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 1, 2)

    def testRectangle_negative_x(self):
        """
        Test creating an instance of Rectangle with negative x argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 2)

    def testRectangle_negative_y(self):
        """
        Test creating an instance of Rectangle with negative y argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 1, -2)

    def testRectangle_area(self):
        """
        Test the area() method of Rectangle.
        """
        r = Rectangle(5, 10, 1, 2)
        self.assertEqual(r.area(), 50)

    def testRectangle_display(self):
        """
        Test the display() method of Rectangle.
        """
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch("sys.stdout", new=StringIO()) as fake_output:
            r.display()
            self.assertEqual(fake_output.getvalue(), expected_output)

    def testRectangle_str(self):
        """
        Test the __str__() method of Rectangle.
        """
        r = Rectangle(5, 10, 1, 2, 123)
        expected_output = "[Rectangle] (123) 1/2 - 5/10"
        self.assertEqual(str(r), expected_output)

    def testRectangle_valid_arguments(self):
        """
        Test creating an instance of Rectangle with valid arguments.
        """
        r = Rectangle(5, 10, 1, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    # Other existing tests...

    def testRectangle_update(self):
        """
        Test the update() method of Rectangle.
        """
        r = Rectangle(5, 10, 1, 2, 123)
        r.update(456, 7, 8, 9, 10)
        self.assertEqual(r.id, 456)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

        r.update(789)
        self.assertEqual(r.id, 789)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

        r.update()
        self.assertEqual(r.id, 789)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)


if __name__ == '__main__':
    unittest.main()
