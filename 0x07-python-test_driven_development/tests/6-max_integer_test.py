#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_result(self):
        self.assertAlmostEqual(max_integer([5, 2, -6]), 5)
        self.assertAlmostEqual(max_integer([2, 5, -6]), 5)
        self.assertAlmostEqual(max_integer([-6, 2, 5]), 5)
        self.assertAlmostEqual(max_integer([93.5]), 93.5)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([0, 0, 0, 0]), 0)
