from Utilities import Turret, Types, Aiming
import cv2
import numpy as np
import json



sx = 3840
sens = 1.5
sy = 2160
ox = (sx/2) - (640/2)
oy = (sy/2) - (480/2)
main = Turret.Turret("Main")
kernel = np.ones((5, 5), 'uint8')
defaultObject = 0
settings = ""
with open("config.json", "r") as f:
    settings = json.load(f)


def clamp(value, min, max):
  return int(sorted((min, value, max))[1])

def FrameFunction(Frame, LastFrame):
  #print(Frame.shape, (int(Frame.shape[0]/2),int(Frame.shape[1]/2)))

  if main.rx > 359:
    main.rx = 0
  main.rx += 3

  main.Objects = main.getObjects(Types.Detections.COLOR)
  #main.Objects = main.getObjects()
  #redMask = cv2.dilate(redMask, kernel, iterations=4)

  editImage = Frame.copy()

  largest = defaultObject
  for object in main.Objects:
    if largest == 0:
      largest = object
    if cv2.contourArea(object.Contour) > 1000:
      if object.Size > largest.Size:
        largest = object

  
  if largest != 0:
    largest.render(editImage)
    Aiming.aim(main, largest)
    pass
  #largest.render(Frame)
  Aiming.start()
  return editImage

main.FrameFunction = FrameFunction

#main.calibrate()
main.start()