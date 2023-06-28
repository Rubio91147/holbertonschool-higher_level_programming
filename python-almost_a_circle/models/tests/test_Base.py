#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def testBase_default(self):

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def testBase_string_argument(self):
        """
        Test creating an instance of Base with a string as the ID argument.
        """
        b = Base("abc")
        self.assertEqual(b.id, "abc")


    def testBase_infinity_argument(self):
        """
        Test creating an instance of Base with infinity as the ID argument.
        """
        b6 = Base(float('inf'))
        self.assertEqual(b6.id, float('inf'))


if __name__ == '__main__':
    unittest.main()
