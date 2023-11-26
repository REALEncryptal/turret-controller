import cv2
from Utilities import eCV
from random import randint as ri

def update(self):
  ## proccessing stuff
  self.toGray()
  self.show()

capture = eCV.CaptureReader("Test", update)
capture.start()