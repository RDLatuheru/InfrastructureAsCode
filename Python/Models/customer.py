# Model class to initiate a customer object

from Models.server import server

class customer:
    id: int
    name: str
    servers: list[server]

    def __init__(self, name):
        self.name = name