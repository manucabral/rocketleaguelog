# rocketleaguelog
A simple and fast Rocket League Log parser.

It can be used to get info about the current map or player without using external mods.


```py
>>> import rocketleaguelog
>>> session = rocketleaguelog.Session()
>>> session.platform()
'Steam'
>>> session.version()
'230620.44144.425548'
>>> session.maps()
[Map(name=MENU), Map(name=Stadium_Foggy_P), Map(name=TrainStation_P), Map(name=MENU)]
>>> session.player()
Player(name=NightNight29)
>>> session.game_running()
False
```
