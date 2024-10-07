# configure an appsettings.py (see appsettings-template)

# Requirements:
    - pip install paho-mqtt
    - pip install python-vlc
    - pip install youtube-dl
    - sudo apt install bluetooth bluez python3-bluez

# on raspi:
    python3 -m venv myenv
    source myenv/bin/activate
    then install

# to run:
    source myenv/bin/activate
    python main.py

# json example
## for local:
    ```
    {
    "typ":"audio",
    "msg":"local",
    "params":[
        "a1"
    ],
    "max_playing_minutes": 5,
    "shuffle": 1
    }
    ```

## for youtube:
    ```
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
    ```