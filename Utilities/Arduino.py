
import Utilities.Types as Enum
import serial

"""
S = Servo
M = Motor to speed  
"""

class Arduino:
  def __init__(self):
    self.SERIAL = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    self.SERIAL.reset_input_buffer()
    self.SerialBuffer = ""

    self.mSent = False
    self.sSent = False

  def Motor(self,speed):
    self.SerialBuffer += str(speed) + "M"
    self.mSent = True

  def Servo(self, angle):
    self.SerialBuffer += str(angle) + "S"
    self.sSent = True

  def SendCommands(self):
    if not self.mSent:
      self.SerialBuffer = self.SerialBuffer + "2M"
    if not self.mSent:
      self.SerialBuffer = "0S" + self.SerialBuffer
   
    input = self.SerialBuffer + "\n"

    self.SERIAL.write(input.encode('utf-8'))

  def reset_buffer(self):
    self.SerialBuffer = ""
    self.mSent = False
    self.sSent = False

  

    

