# -*- coding: utf-8 -*-
"""
Change to Gray Scale
"""
from graphics1 import *


def changeToGray (pic):
    """Returns a grayscale equivalent of an Image object (pic)""" 
 #get dimensions of picture
    height = pic.getHeight()
    width=pic.getWidth()
#Change to grayscale
    for i in range(0,width):
        for j in range(0,height):
            r,g,b = pic.getPixel(i,j)
            bright=int(round(0.299*r+0.587*g+0.114*b))
            grayish=color_rgb(bright,bright,bright)
            pic.setPixel(i,j,grayish)
    return pic

KK=Image(Point(200,200),'KK.gif')
KKg = changeToGray(KK)