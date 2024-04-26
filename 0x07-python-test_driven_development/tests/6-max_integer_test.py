#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_result(self):
       self.assertAlmostEqual(max_integer([2, 5, -6]), 5)
       self.assertAlmostEqual(max_integer([93.5, 183.0, 164.32]), 183.0)
       self.assertAlmostEqual(max_integer([]), None)
       self.assertAlmostEqual(max_integer([0, 0, 0, 0]), 0)
    def test_param(self):
        self.assertRaises(TypeError, max_integer, (1, 3, 5))
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, "star")
        self.assertRaises(TypeError, max_integer, 5)
    def test_values(self):
        self.assertRaises(ValueError, max_integer, [True, 82, 42])
        self.assertRaises(ValueError, max_integer, [97, 1+5j, 69])
        self.assertRaises(ValueError, max_integer, ["sam", 25, 42])
        self.assertRaises(ValueError, max_integer, [15, 28, [12, 4]])

