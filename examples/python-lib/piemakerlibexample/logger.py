"""Logger for PiemakerLibExample."""
from conflog import Conflog

def init():
    """Initialize logger.
    """

    cfl = Conflog(
        conf_dict={
            'level': 'info',
            'format': '[piemakerlibexample] %(levelname)s %(message)s'
        }
    )

    return cfl.get_logger(__name__)
