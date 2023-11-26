import Utilities.Arduino as ARD
import json

Arduino = ARD.Arduino()
settings = ""
with open("config.json", "r") as f:
    settings = json.load(f)

ServoAngle = 90
Arduino.Servo(ServoAngle)

def aim(Turret, Object):
  Arduino.reset_buffer()

  X, Y, W, H = Object.GetProperties()
  XMiddle, YMiddle = Turret.GetMiddles()

  X += W/2
  Y += H/2

  if X > XMiddle:
    Arduino.Motor(1)
  if X < XMiddle:
    Arduino.Motor(-1)
  
  if Y > YMiddle:
    ServoAngle -= 2
  if Y < YMiddle:
    ServoAngle += 2

  Arduino.Servo(ServoAngle)

def start():
  Arduino.SendCommands()



