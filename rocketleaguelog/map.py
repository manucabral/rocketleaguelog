"""
rocketleaguelog.map
-----------------

This module contains the Map information class.
"""


class Map:
    """
    A class used to represent a map.

    Attributes
    ----------
    name : str
        The name or "id" of the map.
    game : str
        The game mode of the map, soccer, hoops, dropshot, etc.
    freeplay : bool
        Whether or not the map is in freeplay.

    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        # pylint: disable=no-member
        return f"Map(name={self.name})"

    def __str__(self):
        # pylint: disable=no-member
        return self.__repr__()
