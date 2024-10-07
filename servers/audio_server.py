import json
import paho.mqtt.client as mqtt

from classes.player.youtub_player import YoutubePlayer
from classes.player.local_player import LocalPlayer
from servers.server_base import ServerBase
from classes.bluetooth.bluetooth import Bluetooth

class AudioServer(ServerBase):
    def __init__(self):
        super().__init__("audio")
        connected= Bluetooth().connect()
        if connected == True:
            print("Bluetooth has connected.")
        elif connected == False:
            print("Cannot connect to bluetooth.")
        else:
            pass
        
    def _run_command(self, cmd):
        if('max_playing_minutes' in cmd.extra):
            max_playing_minutes = cmd.extra['max_playing_minutes']
        else:
            max_playing_minutes = None
        if('shuffle' in cmd.extra):
            shuffle = cmd.extra['shuffle']
        else:
            shuffle = True
        print('shuffle: ' + str(shuffle))

        msg = cmd.msg
        if(msg  == 'youtube'):
            urls = cmd.params
            print(str(cmd.extra.keys()))
            print('youtube: ')
            print('urls: ' + str(urls))
            self.play_youtube(urls, max_playing_minutes=max_playing_minutes, shuffle=shuffle)
            return
        if(msg  == 'local'):
            playlist = cmd.params[0]
            dir = f"audio/{playlist}"
            print(f'Loading local audios from {dir}')
            print('playlist: ' + str(playlist))
            self.play_loacl(dir, max_playing_minutes=max_playing_minutes, shuffle=shuffle)            
            return
        else:
            print(f'Error: msg ({msg}) is not known.')
            
    def play_youtube(self, urls, max_playing_minutes, shuffle):
        YoutubePlayer(urls, max_playing_minutes, shuffle).play_all()
    def play_loacl(self, dir, max_playing_minutes, shuffle):
        LocalPlayer(dir, max_playing_minutes, shuffle).play_all()