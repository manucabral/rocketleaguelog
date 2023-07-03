"""
rocketleaguelog.player
-----------------

This module contains the Player information class.
"""
# TODO: parse keys to lower case, add properties and more.


class Player:
    """
    A class used to represent a player.

    Attributes
    ----------
    PlayerName : str
        The name of the player.
    PlayerID : str
        The ID of the player. (e.g. 'Steam|1343124324345|0')
    LoginStatus : str
        The login status of the player. (e.g. 'LS_LoggedIn'')
    IsPrimary : str
        Whether or not the player is the primary player. (e.g. 'True')
    IsInParty : str
        Whether or not the player is in a party. (e.g. 'False')
    """

    def __init__(self, **kwargs):
        # pylint: disable=unused-argument
        self.__dict__.update(kwargs)

    def __repr__(self):
        # pylint: disable=no-member
        return f"Player(name={self.PlayerName})"

    def __str__(self):
        # pylint: disable=no-member
        return self.__repr__()
