import yt_dlp
from datetime import datetime
from classes.player.player_base import PlayerBase

class YoutubePlayer(PlayerBase):
# URL of the YouTube video
    def __init__(self, urls, max_playing_minutes, shuffle):
        super().__init__(urls=urls, max_playing_minutes=max_playing_minutes, shuffle=shuffle)
    
    def _play_one(self, url, remaining_sec):
        # Create a yt-dlp object and extract video info
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
            return
        print("remaining_sec: "+str(remaining_sec))
        self._play_vlc(best_format, remaining_sec)
