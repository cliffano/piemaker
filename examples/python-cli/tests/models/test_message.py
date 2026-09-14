# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,duplicate-code,too-many-locals
import unittest
from piemakerexample.models.message import Message

class TestMessage(unittest.TestCase):

    def test_getters(self):
        message = Message('Hello World')
        self.assertEqual(message.get_text(), 'Hello World')

    def test_reverse(self):
        message = Message('Hello World')
        message.reverse()
        self.assertEqual(message.get_text(), 'dlroW olleH')

    def test_upper(self):
        message = Message('Hello World')
        message.upper()
        self.assertEqual(message.get_text(), 'HELLO WORLD')

    def test_lower(self):
        message = Message('Hello World')
        message.lower()
        self.assertEqual(message.get_text(), 'hello world')

    def test_str(self):
        message = Message('Hello World')
        self.assertEqual(str(message), 'Hello World')
