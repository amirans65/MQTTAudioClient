import json
import paho.mqtt.client as mqtt

from classes.youtub_player import YoutubePlayer
from servers.server_base import ServerBase

class AudioServer(ServerBase):
    def __init__(self):
        super().__init__("audio")
        
    def _run_command(self, cmd):
        msg = cmd.msg
        if(msg  == 'youtube'):
            urls = cmd.params
            print(str(cmd.extra.keys()))
            if('max_minute' in cmd.extra):
                max_minute = cmd.extra['max_minute']
            else:
                max_minute = None
            print('youtube: ')
            print('max_minute: ' + str(max_minute))
            print('urls: ' + str(urls))
            self.play_youtube(urls, max_minute)
        else:
            print(f'Error: msg ({msg}) is not known.')
            
    def play_youtube(self, urls, max_minute):
        YoutubePlayer(urls, max_minute).play_all()
