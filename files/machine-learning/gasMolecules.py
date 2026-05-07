#Mixing of gas molecules

from graphics import *
from random import uniform,randint
from math import sqrt
def distance(p1,p2):
    return sqrt((p1.getX() - p2.getX())**2 + (p1.getY() - p2.getY())**2)

class Molecule():
    
    def __init__(self,x,y):
        
        self.pict = Circle(Point(x,y),0.5)
        self.pict.setFill('red')
        self.color = 'red'
    def setColor(self,col):
        self.color =col
        self.pict.setFill(col)
    def getColor(self):
        return self.color
        
#Gas Molecule Mixing Animation
win = GraphWin('Gas Molecules', 600,600)
win.setCoords(-100,-100,100,100)
wall = Line(Point(0,-100),Point(0,100))
wall.draw(win)
blackHole = Circle(Point(-30,50),20)
blackHole.draw(win)
blackHole.setFill('black')
gas =[]
for i in range(1000):
    m = Molecule(uniform(1,100),uniform(-100,100))
    m.pict.draw(win)
    gas.append(m)
win.getMouse()
wall.undraw()
for i in range(500):
    for mol in gas:
        if mol.getColor() != 'yellow':
            mol.pict.move(randint(-6,6),randint(-6,6))
        if mol.pict.getCenter().getX()> 99:
            mol.pict.move(-1,0)
        if mol.pict.getCenter().getY()> 99:
            mol.pict.move(0,-1)
        if mol.pict.getCenter().getY()< -99:
            mol.pict.move(0,1)
        if mol.pict.getCenter().getX() < 0 and mol.getColor()=='red':
            mol.setColor('blue')
        if mol.pict.getCenter().getX() > 0 and mol.getColor() == 'blue':
            mol.setColor('green')
          
        if distance(mol.pict.getCenter(),blackHole.getCenter()) <= blackHole.getRadius():
            mol.setColor('yellow')
           
        
win.getMouse()    
win.close()