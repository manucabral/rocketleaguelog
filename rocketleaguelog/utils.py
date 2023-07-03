"""
rocketleaguelog.utils
---------------------

This module provides utility functions that are used internally.
"""
import os
from .constants import Constants


def get_default_log_path() -> str:
    """
    Returns the default path to Rocket League log files.

    Returns
    -------
    str
        The default path to Rocket League log files.

    """
    return os.path.join(
        os.path.expanduser(Constants.DEFAULT_LOG_PATH), Constants.DEFAULT_LOG_NAME
    )


def get_last_token(lines: list, token: str) -> str:
    """
    Returns the last token from a list.

    Parameters
    ----------
    lines : list
        Specifies the list of lines to search.
    token : str
        Specifies the token to search for.

    Returns
    -------
    str
        The last token from the list.

    """
    line = next(filter(lambda line: token in line, lines[::-1]), None)
    if line is None:
        return None
    return line
