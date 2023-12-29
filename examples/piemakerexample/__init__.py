# pylint: disable=too-many-locals
"""
piemakerexample
=======
Example Python package for PieMaker
"""

import click

def hello() -> None:
    """Say hello."""

    print('Hellooo')

@click.command()
def cli() -> None:
    """Python CLI example.
    """
    hello()
