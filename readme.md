# MQTT Audio Client
This tool is for running an MQTT client to manage MQTT requests for
playing local and youtube audios/videos. 

Tested on Windows11 and Rasbian-raspi3 (should also work on Mac and Linux).

# Requirements:
configure first an appsettings.py (see appsettings-template.json)

## On raspi:
    python3 -m venv myenv
    source myenv/bin/activate
    then install

## Install
    - pip install paho-mqtt
    - pip install python-vlc
    - pip install yt-dlp
    - sudo apt install bluetooth bluez python3-bluez

# To run:
    source myenv/bin/activate
    python main.py

# MQTT json example
## for local
    {
        "typ":"audio",
        "msg":"local",
        "params":[
            "playlist1"
        ],
        "max_playing_minutes": 5,
        "shuffle": 1
    }

## for youtube
    {
        "typ":"audio",
        "msg":"youtube",
        "params":[
            "https://www.youtube.com/watch?v=OZ2TkfYrz5o",
            "https://www.youtube.com/watch?v=vw4tlY7kCeg",
            "https://www.youtube.com/watch?v=PeTZJIKkH6Q"
        ],
        "max_playing_minutes": 5,
        "shuffle": 1
    }

# Todos:
- cache youtube locally to not download everytime
- add "immidiate stop" request
- support volume controls and track controls
- add local logger and upload log request
- add watchdog service 
- add Microphone support
- support ChatGPT

