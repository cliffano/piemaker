# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
from piemakerexample import hello


class TestPieMakerExample(unittest.TestCase):

    def test_hello(self):
        hello()
