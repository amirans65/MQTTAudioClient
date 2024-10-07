from datetime import datetime
from classes.player.player_base import PlayerBase

class LocalPlayer(PlayerBase):
    def __init__(self, dir, max_playing_minutes, shuffle):
        super().__init__(dir=dir, max_playing_minutes=max_playing_minutes, shuffle=shuffle)
    
    def _play_one(self, url, remaining_sec):
        print("remaining_sec: "+str(remaining_sec))
        self._play_vlc(url, remaining_sec)
