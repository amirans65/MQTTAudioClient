import paho.mqtt.client as mqtt
import json
from commands.command_builder import CommandBuilder
from classes.settings import Settings

class ServerBase:
    root_topic = "rpi"
    topic = ''
    def __init__(self, sub_topic):
        self.topic = f"{self.root_topic}/{sub_topic}"
        self.last_message = ''
        self.settings = Settings()

    @staticmethod
    def is_valid_json(text):
        try:
            json.loads(text)
            return True
        except ValueError:
            return False
    
    def on_connect_builder(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code " + str(rc))
            client.subscribe(self.topic)
            client.publish(self.topic, "I am Connected.")
        return on_connect

    def on_message_builder(self):
        def on_message(client, userdata, msg):
            self.last_message = msg
            print(f'received msg: [{msg.topic}] {str(msg.payload)}')
            if(self.is_valid_json(msg.payload)):
                print('valid json has been received' + str(msg.payload))
                command = CommandBuilder().build(msg.payload)
                if(command is not None):
                    self.on_command(command)
        return on_message 

    def on_command(self, command):
        print('command: ' + str(command))
        self._run_command(command)
    def _run_command(self, command):
        raise NotImplementedError('Implement __run_command in subclass')
            

    def connect(self):
        self.client = mqtt.Client()
        self.client.username_pw_set(self.settings.mqtt_username, self.settings.mqtt_password)
        self.client.on_connect = self.on_connect_builder()
        self.client.on_message = self.on_message_builder()

        self.client.connect(self.settings.mqtt_ip, self.settings.mqtt_port, 60)
        self.client.loop_forever()