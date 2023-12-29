# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from unittest.mock import patch, call
import unittest.mock
import unittest
from piemakerexample import hello

class TestPieMakerExample(unittest.TestCase):

    @patch('builtins.print')
    def test_hello( # pylint: disable=too-many-arguments
            self,
            func_print):

        hello()
        assert func_print.mock_calls == [call('Hellooo')]
