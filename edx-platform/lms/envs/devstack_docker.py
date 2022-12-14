"""
Left over environment file from before the transition of devstack from
vagrant to docker was complete.

This file should no longer be used, and is only around in case something
still refers to it.
"""

from .devstack import *  # pylint: disable=wildcard-import, unused-wildcard-import

LOGGING['handlers']['tracking'] = {
    'level': 'DEBUG',
    'class': 'logging.FileHandler',
    'filename': '/edx/var/log/tracking/tracking.log',
    'formatter': 'raw',
}

LOGGING['loggers']['tracking']['handlers'] = ['tracking']
