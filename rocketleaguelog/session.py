"""
rocketleaguelog.session
-----------------

This module contains the Session class that manages the information of a Rocket League log file.

"""
import os
from .map import Map
from .player import Player
from .utils import get_default_log_path, get_last_token


class Session:
    """
    A session represents a single Rocket League log file.

    Parameters
    ----------
    path : str
        Specifies the path to a Rocket League log file.

    Returns
    -------
    Session
        A session object.

    Raises
    ------
    FileNotFoundError : If the specified path does not exist.

    Examples
    --------
    >>> import rocketleaguelog
    >>> session = rocketleaguelog.Session()

    """

    def __init__(self, path: str = None):
        # pylint: disable=unused-argument
        path = path or get_default_log_path()
        if not os.path.exists(path):
            raise FileNotFoundError(f"Log path {path} does not exist.")
        self.__path = path
        self.__data = self.__read()

    def __repr__(self) -> str:
        # pylint: disable=no-member
        path = os.path.normpath(self.path)
        return f"Session(path='{'...' + path[-20:]}')"

    def __str__(self) -> str:
        # pylint: disable=no-member
        return self.__repr__()

    @property
    def path(self) -> str:
        """
        Returns the path to the Rocket League log file.

        Returns
        -------
        str
            The path to the Rocket League log file.

        """
        return self.__path

    def __read(self) -> str:
        """
        Reads the Rocket League log file.

        Returns
        -------
        str
            The contents of the Rocket League log file.

        """
        with open(self.__path, "r", encoding="utf-8", errors="ignore") as log_file:
            raw_data = map(lambda line: line.strip(), log_file.readlines())
            return list(
                filter(
                    lambda line: "Log:" in line
                    or "Party:" in line
                    or "Init:" in line
                    or "DevOnline:" in line
                    or "Base directory:" in line
                    and not "load package:" in line,
                    raw_data,
                )
            )

    def __parse_map(self, _map: str) -> Map:
        """
        Parses a map string into a Map object.

        Parameters
        ----------
        _map : str
            The map string to parse.

        Returns
        Map
            A Map object.

        """
        if "MENU" in _map:
            return Map(name="MENU", game="MENU", freeplay=False)
        return Map(
            name=(
                _map[: _map.find("?")]
                if not "/" in _map  # onlinematch
                else _map[_map.find("/") + 1 : _map.find("?")]
            ),
            game=dict(line.split("=") for line in _map.split("?") if "=" in line).get(
                "game", "Unknown"
            ),
            freeplay="Freeplay" in _map,
        )

    def platform(self) -> str:
        """
        Returns the game's platform.

        Returns
        -------
        str
            The game's platform.

        """
        token = "Base directory:"
        line = get_last_token(self.__data, token)
        if line is None:
            return "Unknown"
        return line.partition(token)[2].strip().split("\\")[2]

    def version(self) -> str:
        """
        Obtains the build version of the game.

        Returns
        -------
        str
            The build version of the game.

        """
        return self.__data[7].partition("Version:")[2].strip()

    def player(self) -> Player:
        """
        Obtains the player's information.

        Returns
        -------
        Player
            A Player object.

        """
        token = "HandleLocalPlayerLoginStatusChanged"
        line = get_last_token(self.__data, token)
        values = {}
        pairs = line.split()
        for pair in pairs:
            key_value = pair.split("=")
            if len(key_value) == 2:
                key, value = key_value
                values[key] = value
        values["PlayerName"] = line[
            line.find("PlayerName=") + len("PlayerName=") : line.find("PlayerID=")
        ].strip()
        return Player(**values)

    def game_running(self) -> bool:
        """
        Checks if Rocket League is currently running.

        Returns
        -------
        bool
            True if Rocket League is running, False otherwise.

        """
        return get_last_token(self.__data, "Log file closed") is None

    def maps(self) -> list:
        """
        Returns the maps played or currently being played in the session.

        Returns
        -------
        list
            A list of Map objects.

        """
        return [
            self.__parse_map(line.partition("LoadMap:")[2].strip())
            for line in self.__data
            if "LoadMap:" in line
            and not "JoinGameTransition" in line  # exclude joining a game
        ]
