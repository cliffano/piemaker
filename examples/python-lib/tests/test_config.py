# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from unittest.mock import patch, mock_open
import unittest.mock
import unittest
import yaml
from piemakerlibexample.config import load

CONFIG_WITH_PROPERTIES = '''
---
text: Hello World
'''

CONFIG_WITHOUT_VALUES = '''
---
text:
'''

CONFIG_EMPTY = '''
'''

CONFIG_INVALID = '''
foo bar:
  & whoa
'''

class TestConfig(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=CONFIG_WITH_PROPERTIES)
    @patch('piemakerlibexample.config.init')
    def test_load_with_properties(self, func_init, func_open): # pylint: disable=unused-argument
        with open('piemakerlibexample.yaml', 'r', encoding='utf8') as file_handle:
            assert file_handle.read() == CONFIG_WITH_PROPERTIES

        mock_logger = unittest.mock.Mock()

        func_init.return_value = mock_logger

        conf = load('piemakerlibexample.yaml')
        self.assertEqual(conf['text'], 'Hello World')

    @patch('builtins.open', new_callable=mock_open, read_data=CONFIG_WITHOUT_VALUES)
    @patch('piemakerlibexample.config.init')
    def test_load_without_values(self, func_init, func_open): # pylint: disable=unused-argument
        with open('piemakerlibexample.yaml', 'r', encoding='utf8') as file_handle:
            assert file_handle.read() == CONFIG_WITHOUT_VALUES

        mock_logger = unittest.mock.Mock()

        func_init.return_value = mock_logger

        conf = load('piemakerlibexample.yaml')
        self.assertEqual(conf['text'], None)

    @patch('builtins.open', new_callable=mock_open, read_data=CONFIG_EMPTY)
    @patch('piemakerlibexample.config.init')
    def test_load_empty_config(self, func_init, func_open): # pylint: disable=unused-argument
        with open('piemakerlibexample.yaml', 'r', encoding='utf8') as file_handle:
            assert file_handle.read() == CONFIG_EMPTY

        mock_logger = unittest.mock.Mock()

        func_init.return_value = mock_logger

        conf = load('piemakerlibexample.yaml')
        self.assertEqual(conf, None)

    @patch('builtins.open', new_callable=mock_open, read_data=CONFIG_INVALID)
    def test_load_invalid_config(self, func_open): # pylint: disable=unused-argument
        with open('piemakerlibexample.yaml', 'r', encoding='utf8') as file_handle:
            assert file_handle.read() == CONFIG_INVALID
        with self.assertRaises(yaml.scanner.ScannerError):
            load('piemakerlibexample.yaml')
