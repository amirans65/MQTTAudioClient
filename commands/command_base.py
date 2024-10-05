class CommandBase:
    def __init__(self,  typ='', msg='', params=[], **extra):
      self.typ = str(typ)
      self.msg = str(msg)
      self.params = params
      self.extra = extra
      
    def __str__(self) -> str:
        return "Command with:\n"+str(self.__dict__)