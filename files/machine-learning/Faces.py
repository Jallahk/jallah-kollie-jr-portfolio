
import math
from perceptronClass import *
from graphics1 import *
from grayscale import *

win1=GraphWin("Face1",500,500)
F1=Image(Point(200,200),'Face1a.gif')
F1.draw(win1)

win2=GraphWin("Face2",500,500)
F2=Image(Point(200,200),'Face2.gif')
F2.draw(win2)

win3=GraphWin("Face3",500,500)
F3=Image(Point(200,200),'Face3.gif')
F3.draw(win3)

win4=GraphWin("Face4",500,500)
F4=Image(Point(200,200),'Face2p.gif')
F4.draw(win4)

win5=GraphWin("Face5",500,500)
F5=Image(Point(200,200),'Face2blocked.gif')
F5.draw(win5)
#KK=Image(Point(200,200),'KK.gif')
#win6=GraphWin("KKFace",500,500)
#KK.draw(win6)
for win in [win1,win2,win3,win4,win5]:
    win.getMouse()
    win.close()
face1 =[]
face2 =[]
face3 =[]
face4 =[]
face5 = []
#faceKK =[]


for xpix in range(0,160):
    for ypix in range(0,200):
        F1pix=F1.getPixel(xpix,ypix)
        F2pix=F2.getPixel(xpix,ypix)
        F3pix = F3.getPixel(xpix,ypix)
        F4pix = F4.getPixel(xpix,ypix)
        F5pix = F5.getPixel(xpix,ypix)
        #FKKpix = KK.getPixel(xpix,ypix)
        
        face1+=F1pix
        face2+=F2pix
        face3+=F3pix
        face4+=F4pix
        face5+=F5pix
        #faceKK+=FKKpix
       
        

face1 += [1]
face2 += [0]
face3 += [1]

faces =[face1,face2,face3]
q=Perceptron(96000,step)
q.train(faces,0.5)




