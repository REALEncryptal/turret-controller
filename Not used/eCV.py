import cv2
import numpy as np

def invertMask(mask):
    """
    Returns the inverted version of the mask.
    """
    return cv2.bitwise_not(mask) # Invert the mask

class CaptureReader():
  """
    Class to stream video and do stuff with it
  """
  def __init__(self, Name = "Capture", frameFunction = False):
    self.Name = Name
    self.FrameFunction = frameFunction
  
    # Initialize the camera and creates varibles
    self.Capture = cv2.VideoCapture(0)

    self.Capture.set(3, 1920)
    self.Capture.set(4, 1080)

    
    _, Frame = self.Capture.read()

    
    self.Frame = Frame
    self.LastFrame = Frame # set the last frame to avoid errors

    self.CurrentFrameIsGray = False
    self.CanRun = True
    self.isAlive = True
    
  def __del__(self):
    print("Removed CaptureReader Object")
    pass
  
  ## Get the frame from the camera
  def getFrame(self):
    _, Frame = self.Capture.read()
    self.CurrentFrameIsGray = False

    return Frame

  def show(self):
    cv2.imshow(self.Name, self.Frame)

  ## UTILITIES

  #returns
  def getToGray(self): 
    self.CurrentFrameIsGray = True
    return cv2.cvtColor(self.Frame.copy(), cv2.COLOR_BGR2GRAY) # get a version of the frame that is gray

  def getDilated(self, size = 5, iterations = 1, getorset = "get"):
    frame = None
    if getorset == "get": #
      frame = self.Frame.copy()
    else:
      frame = self.Frame

    return cv2.dilate(
      frame,
      np.ones((size, size), 'uint8'),
      iterations = iterations
    )

  def getEroded(self, size = 5, iterations = 1, getorset = "get"):
    frame = None
    if getorset == "get":
      frame = self.Frame.copy()
    else:
      frame = self.Frame

    return cv2.erode(
      frame,
      np.ones((size, size), 'uint8'),
      iterations = iterations
    )

  # setters

  def toGray(self):
    self.CurrentFrameIsGray = True
    self.Frame = cv2.cvtColor(self.Frame, cv2.COLOR_BGR2GRAY) # change the frame to grayscale
  
  # Start recieving frames
  def start(self):
    while self.isAlive:
      if self.CanRun:
        self.Frame = self.getFrame() # get new frame from camera

        if self.FrameFunction != False: # if there is a function to run
          self.FrameFunction(self) # run the function

        self.LastFrame = self.Frame # set last frame at the end of the processing

        key = cv2.waitKey(1)
        if key == 27:# if the key is esc
            self.isAlive = False # set to dead
            break# break out of the loop