# pylint: disable=too-many-locals
"""
Example Python package built with PieMaker and Click.
"""

import click


def hello() -> None:
    """Print a greeting message to standard output.

    :rtype: None
    """

    print("Hellooo")


@click.command()
def cli() -> None:
    """Entry point for the CLI.

    Invokes :func:`hello` to print a greeting.

    :rtype: None
    """
    hello()
