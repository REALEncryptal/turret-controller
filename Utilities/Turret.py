from Utilities.Object import Object
from Utilities import Types
import cv2
import numpy as np
from enum import Enum

class Turret:
  def __init__(self, Name):
    self.Name = Name
    
    self.Capture = cv2.VideoCapture(0)

    _, Frame = self.Capture.read()
    rows, cols, _ = Frame.shape

    self.Frame = cv2.flip(Frame, 1)
    self.LastFrame = self.Frame ## just to prevent errors on the first frame
    self.Rows = rows
    self.Cols = cols
  
    self.XMiddle = int(cols / 2)
    self.YMiddle = int(rows / 2)
    self.wThresh = 0
    self.hThresh = 0

    self.FrameFunction = False
    self.Objects = []

    self.ServoPos = 90
    self.State = Types.States.IDLE
    self.Started = False

    self.rx = 0
  
  def start(self):
    if not self.Started and not self.State == Types.States.SHUTDOWN:
      while not self.State == Types.States.SHUTDOWN:
        _, Frame = self.Capture.read()
        self.Frame = cv2.flip(Frame, 1)

        if self.FrameFunction != False:
          Frame = self.FrameFunction(self.Frame, self.LastFrame)

        cv2.imshow(str(self.Name), Frame)
        self.LastFrame = self.Frame
        cv2.imshow(str(self.Name + " LAST FRAME"), self.LastFrame)
        key = cv2.waitKey(1)
        if key == 27:
            break

  def GetMiddles(self):
    return self.XMiddle, self.YMiddle

  def getObjects(self, Detections, Thresh = 0):
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    hsv_frame = cv2.cvtColor(self.Frame, cv2.COLOR_BGR2HSV)
    
    if Detections == Types.Detections.COLOR: ######## Color DETECTON
      red_mask = cv2.inRange(hsv_frame, low_red, high_red)
      contours, _ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)## get red stuff
      objects = []
      for cnt in sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True):
        (x, y, w, h) = cv2.boundingRect(cnt) 
        objects.append(Object(x+int((w/2)),y+int((h/2)),w,h, cnt, self.Frame, self.rx))
      
      return objects

    elif Detections == Types.Detections.MOTION or Detections == Types.Detections.DIFFERENCE: ######## Motion/Difference DETECTON
      Frame = cv2.cvtColor(self.Frame, cv2.COLOR_RGB2GRAY)
      LastFrame = cv2.cvtColor(self.LastFrame, cv2.COLOR_RGB2GRAY)

      diff_frame = cv2.absdiff(src1=LastFrame, src2=Frame)
    
      kernel = np.ones((40, 40))
      diff_frame = cv2.dilate(diff_frame, kernel, 1)

      thresImage = cv2.threshold(src=diff_frame, thresh=Thresh, maxval=255, type=cv2.THRESH_BINARY)[1]

      contours, _ = cv2.findContours(image=thresImage, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

      objects = []
      for cnt in sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True):
        (x, y, w, h) = cv2.boundingRect(cnt) 
        objects.append(Object(x+int((w/2)),y+int((h/2)),w,h, cnt, self.Frame, self.rx))

      return objects



