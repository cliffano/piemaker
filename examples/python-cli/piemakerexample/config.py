"""Configuration loader.
"""
import yaml
from .logger import init

def load(conf_file: str) -> dict:
    """Load configuration values from file.
    """

    logger = init()
    logger.info(f'Loading configuration file {conf_file}')

    conf = {}
    with open(conf_file, 'r', encoding='utf-8') as stream:
        conf = yaml.load(stream, Loader=yaml.FullLoader)

    return conf
