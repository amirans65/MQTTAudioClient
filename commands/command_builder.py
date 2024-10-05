import json

from commands.audio_command import AudioCommand

class CommandBuilder:
    def __init__(self):
        pass
    
    def build(self, jsonString):
        data = json.loads(jsonString)
        return self.__convert(data)
    
    def __convert(self, data):
        if('typ' not in data.keys()):
            print ('Error: command type is wrong. It needs to have "typ" field.')
            return None
        typ = str(data['typ']).lower()
        if(typ == 'audio'):
            return AudioCommand(**data)
        print (f'Error: command type is wrong. the "typ" ({typ}) is unknown.')
        return None
