#!/usr/bin/python3
""" module """

import unittest
from main import Base
from unittest.mock import patch
from io import StringIO


class TestBase(unittest.TestCase):

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            b1 = Base(99, 55)

    def test_display(self):
        """ Test string displayed """
        r1 = Base("salah", 27)
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.garbage()
            res = "my name is salah and age 27\n"
            self.assertEqual(str_out.getvalue(), res)


