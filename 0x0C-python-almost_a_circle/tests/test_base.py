#!/usr/bin/python3

import unittest
import json
from models.base import Base


class Test_base(unittest.TestCase):
    def test_equality(self):
        b1 = Base()
        b2 = Base(35)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 35)
        self.assertNotEqual(b1.id, 0)
        self.assertNotEqual(b1.id, b2.id)
        self.assertNotEqual(b1.id, b3.id)
        self.assertEqual(b3.id, 2)
