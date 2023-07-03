"""
Rocket League Log
-----------------

A simple library and fast library for parsing Rocket League log files.

Examples
--------
>>> import rocketleaguelog
>>> session = rocketleaguelog.Session()
>>> session.platform()
'Steam'
>>> session.version()
'230620.44144.425548'
"""
import os
from .metadata import __title__, __description__, __author__, __license__, __version__
from .session import Session

if os.name != "nt":
    raise NotImplementedError("Only Windows systems are supported.")

__all__ = [
    "Session",
    "__title__",
    "__description__",
    "__author__",
    "__license__",
    "__version__",
]
