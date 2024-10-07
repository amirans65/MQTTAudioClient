import yt_dlp
import vlc
import time
from datetime import datetime
import os
import random

class PlayerBase:
# URL of the YouTube video
    def __init__(self, urls=None,dir=None, max_playing_minutes=None, shuffle=True):
        self.max_playing_minutes = max_playing_minutes if max_playing_minutes is not None else float('inf')
        if(urls is not None):
            self.urls = urls
        elif(dir is not None):
            self.urls = self._list_files_walk(dir)
            print("pass:")
            print(str(self.urls))
        if(shuffle):
            random.shuffle(self.urls)
    
    def play_all(self):
        start = datetime.now()
        for url in self.urls:
            now = datetime.now()
            delta_sec = (now - start).total_seconds()
            remaining_sec = self.max_playing_minutes*60 - delta_sec
            if (remaining_sec < 0):
                break
            
            print("base remaining_sec: "+str(remaining_sec))
            self._play_one(url, remaining_sec)
    
    @staticmethod            
    def _list_files_walk(directory):
        directory = os.path.abspath(directory)
        res = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                res.append(os.path.join(root, file))
        return res
            
    def _play_one(self, url, remaining_sec):
        raise NotImplementedError('Should be overriden')
            
    def _play_vlc(self, url, remaining_sec):
        start = datetime.now()
        # Create a VLC media player object
        vlc_instance = vlc.Instance()

        # creating a media player
        player = vlc_instance.media_player_new()
        
        # creating a media
        media = vlc_instance.media_new(url)
        
        # setting media to the player
        player.set_media(media)

        print('playing...')
        # Play the video
        player.play()
        
        # Give VLC some time to start playing
        time.sleep(1)
        
        # Check if the media is playing
        if player.is_playing():
            print("Media is playing")
        else:
            print("Failed to play media")

        # Keep the script running while the video is playing
        while True:
            now = datetime.now()
            delta_sec = (now - start).total_seconds()
            left = remaining_sec - delta_sec
            if left < 0:
                player.stop()
                break
            state = player.get_state()
            if state in [vlc.State.Ended, vlc.State.Error]:
                player.stop()
                break
            time.sleep(1)
            print(f"left: {left}")
