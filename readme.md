# make an appsettings.py (see appsettings-template)
    - mqtt_ip
    - mqtt_port = ""
    - mqtt_username = ""
    - mqtt_password = ""

# Requirements:
    - pip install paho-mqtt
    - pip install python-vlc
    - pip install youtube-dl

# on raspi:
    python3 -m venv myenv
    source myenv/bin/activate
    then install

# to run:
    source myenv/bin/activate
    python main.py