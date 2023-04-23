# Enum to set servertype restrictions

from enum import Enum

class serverType(Enum):
    WEB = 1
    DB = 2
    LB = 3