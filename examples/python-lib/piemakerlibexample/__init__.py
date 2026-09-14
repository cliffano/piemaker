# pylint: disable=too-many-locals,too-few-public-methods
"""
piemakerlibexample
&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;&#x3D;
... .
"""
from .config import load
from .logger import init
from .models.message import Message

class Display():
    """A class for managing the display of text from configuration file."""

    def __init__(self, conf_file: str) -> None:
        """Initialise Display."""

        logger = init()

        logger.info(f'Loading configuration file {conf_file}')
        self.conf = load(conf_file)

    def format(self, reverse: bool, transformation: str) -> str:
        """Format text from configuration file with transformations."""

        message = Message(self.conf['text'])

        if reverse:
            message.reverse()

        if transformation == 'lower':
            message.lower()
        elif transformation == 'upper':
            message.upper()

        return message.get_text()
