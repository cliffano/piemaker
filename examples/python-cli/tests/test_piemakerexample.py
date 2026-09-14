# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
from unittest.mock import patch
import unittest.mock
import unittest
from click.testing import CliRunner
from piemakerexample import display
from piemakerexample import cli

class TestPiemakerExample(unittest.TestCase):

    @patch('piemakerexample.load')
    @patch('piemakerexample.init')
    def test_display( # pylint: disable=too-many-arguments
            self,
            func_init,
            func_load):

        mock_logger = unittest.mock.Mock()

        func_init.return_value = mock_logger
        func_load.return_value = {
            'text': 'Hello World'
        }

        display(conf_file='piemakerexample.yaml', reverse=False, transformation='lower')

    @patch('piemakerexample.load')
    @patch('piemakerexample.init')
    def test_display_with_non_default_args( # pylint: disable=too-many-arguments
            self,
            func_init,
            func_load):

        mock_logger = unittest.mock.Mock()

        func_init.return_value = mock_logger
        func_load.return_value = {
            'text': 'Hello World'
        }

        display(conf_file='piemakerexample.yaml', reverse=True, transformation='upper')

    @patch('piemakerexample.display')
    def test_cli( # pylint: disable=too-many-arguments
            self,
            func_display):

        func_display.return_value = None

        runner = CliRunner()
        result = runner.invoke(cli, [
            '--conf-file',
            'piemakerexample.yaml',
            '--reverse',
            '--transformation',
            'lower'
        ])
        assert not result.exception
        assert result.exit_code == 0
        assert result.output == ''

        # should delegate call to display
        func_display.assert_called_once_with('piemakerexample.yaml', True, 'lower')
