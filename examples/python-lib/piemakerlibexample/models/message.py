"""This module contains the Message class."""

class Message():
    """This class represents a message.
    It contains the message text.
    """

    def __init__(self, text: str) -> None:
        """Initialize the Message object."""
        self.text = text

    def get_text(self) -> str:
        """Return the message text."""
        return self.text

    def reverse(self) -> None:
        """Return the message text in reverse order."""
        self.text = self.text[::-1]

    def lower(self) -> None:
        """Return the message text in lower case."""
        self.text = self.text.lower()

    def upper(self) -> None:
        """Return the message text in upper case."""
        self.text = self.text.upper()

    def __str__(self) -> str:
        """Return the string representation of the Message object."""
        return f'{self.text}'
