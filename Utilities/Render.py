import cv2
import numpy as np
import colorsys


def mT(t,x):
    n = []
    n.append(t[0] * x)
    n.append(t[1] * x)
    n.append(t[2] * x)

    return tuple(n)


def text(font, X,Y, NAME, img):
    cv2.putText(img, NAME, (X,Y), font, .8, (0, 0, 0), 2, cv2.LINE_AA)

def circle(X,Y,R, img):
    cv2.circle(img, (X,Y), R, (255,0,0), -1)

def nameBox(font, W,H,X,Y, NAME, img, rx):
    TOPLEFT = (int((W/2)+X),int((H/2)+Y))
    TOPLEFTTEXT = (X-int((W/2)), Y-int((H/2))-10)
    BOTTOMRIGHT = (X-int((W/2)), Y-int((H/2)))

    cv2.putText(img, NAME, TOPLEFTTEXT, font, .8, mT(colorsys.hsv_to_rgb(rx/360,1,.8), 255), 2, cv2.LINE_AA)
    cv2.circle(img, (X,Y), 5, (80, 80, 255), -1)
    cv2.rectangle(img, TOPLEFT, BOTTOMRIGHT, mT(colorsys.hsv_to_rgb(rx/360,1,.8), 255), 3)

def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def tracer(origin, object, img, rx):
    cv2.line(img, origin, object, mT(colorsys.hsv_to_rgb(rx/360,1,1), 255), 2)

