import json
class Settings:
    def __init__(self):
        with open('appsettings.json', 'r') as file:
            data = json.load(file)
        self.__dict__.update(data)