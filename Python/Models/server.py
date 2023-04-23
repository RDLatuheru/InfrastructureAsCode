# Model class to initiate a server-object

from Models.serverType import serverType
from Models.environment import environment

class server:

    hostname: str
    ip: str
    memory: int
    type: serverType
    env: environment

    @classmethod
    def fromDatabase(self, cls, hostname, ip, memory, type, environment):
        self.hostname = hostname
        self.ip = ip
        self.memory = memory
        self.type = type
        self.env = environment

        return cls()
