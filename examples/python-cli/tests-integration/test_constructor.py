# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
from piemakerexample import display

class TestConstructor(unittest.TestCase):

    def test_constructor_with_lower_non_reverse(self):
        display('examples/piemakerexample.yaml', False, 'lower')

    def test_constructor_with_upper_reverse(self):
        display('examples/piemakerexample.yaml', True, 'upper')
