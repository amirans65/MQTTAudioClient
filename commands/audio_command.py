from commands.command_base import CommandBase

class AudioCommand(CommandBase):
    def __init__(self, msg='', params=[], **extra):
      typ = 'audio'
      if 'typ' in extra:
          del extra['typ']
      super().__init__(typ, msg, params, **extra)
    