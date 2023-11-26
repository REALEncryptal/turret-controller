from enum import Enum

class States(Enum):
    IDLE = 1
    SHOOTING = 2
    TRACKING = 3
    LOOKING = 3
    STARTING = 4
    CALIBRATING = 5
    SHUTDOWN =  5

class Detections(Enum):
    COLOR = 1
    MOTION = 2
    DIFFERENCE = 2

class Communication(Enum):
    MOTOR = 1
    TILT = 2
    POSITION = 3
    CONNECTION = 4

     