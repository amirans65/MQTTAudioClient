import yt_dlp
import vlc
import time
from datetime import datetime

class YoutubePlayer:
# URL of the YouTube video
    def __init__(self, urls, max_playing_minutes=None):
        self.max_playing_minutes = max_playing_minutes if max_playing_minutes is not None else float('inf')
        self.urls = urls
    
    def play_all(self):
        start = datetime.now()
        for url in self.urls:
            now = datetime.now()
            delta_sec = (now - start).total_seconds()
            remaining_sec = self.max_playing_minutes*60 - delta_sec
            if (remaining_sec < 0):
                break
            self.__play_one(url, remaining_sec)
            
    
    def __play_one(self, url, remaining_sec):
        # Create a yt-dlp object and extract video info
        start = datetime.now()
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', None)

        # Check if formats is None
        if formats is None:
            print("Failed to extract video formats")
        else:
            # Print available formats
            for f in formats:
                print(f"Format code: {f['format_id']}, Extension: {f['ext']}, Resolution: {f.get('resolution', 'N/A')}, Audio codec: {f.get('acodec', 'none')}")

            # Select the best format with both audio and video
            best_format = None
            for f in formats:
                if f.get('acodec') != 'none' and f.get('vcodec') != 'none':  # Check if the format has both audio and video codecs
                    best_format = f['url']
                    break

            if best_format is None:
                print("No suitable format with both audio and video found")
            else:
                # Create a VLC media player object
                vlc_instance = vlc.Instance()

                # creating a media player
                player = vlc_instance.media_player_new()
                
                # creating a media
                media = vlc_instance.media_new(best_format)
                
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
