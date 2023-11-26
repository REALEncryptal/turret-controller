import re
from typing_extensions import Self
from Utilities import Render
import cv2
import numpy as np



def rgb_to_hsv(b, g, r):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)*100
    v = mx*100
    return h, s, v



class Object:
  def __del__(self):
    pass
  def __init__(self, X,Y,W,H, Contour, SourceImage, rx):
    self.X = X
    self.Y = Y
    self.W = W
    self.H = H
    self.Contour = Contour
    self.SourceImage = SourceImage
    self.rx = rx

    self.Size = W + H
    #self.Color = np.array(cv2.mean(SourceImage[Y:Y+H,X:X+W])).astype(np.uint8)
    #self.Color = rgb_to_hsv(self.Color)

    self.XCenter = int((self.X + self.X + self.W) / 2)
    self.YCenter = int((self.Y + self.Y + self.H)/2)
  
  def GetProperties(self):
    return self.X, self.Y, self.W, self.H

  def render(self, img):
    Render.nameBox(
      cv2.FONT_HERSHEY_SIMPLEX,
       self.W,
       self.H,
       self.X,
       self.Y,
      "Object",
      img,
      self.rx
    )

    Render.circle(0, 0, 30, img)
    Render.circle(640, 480, 30, img)
    Render.text(
      cv2.FONT_HERSHEY_SIMPLEX,
      480,
      640,
      "MAX",
      img)

    Render.text(
      cv2.FONT_HERSHEY_SIMPLEX,
      self.X,
      self.Y,
      " " + str(self.X) + ", " + str(self.Y),
      img)
    Render.tracer((int(640/2), int(480/2)), (self.X, self.Y), img, 360)
