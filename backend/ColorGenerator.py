from tkinter import *
import math

def findAngle(x,y): 
    radian = math.atan2(y,x)
    print(radian)
    degree = radian * (360/(2*math.pi))
    if (degree < 0): 
        degree = 360 + degree
    print(degree)
    return degree

def findDistance(x,y):
    distance = ((x**2)+(y**2))*0.5
    return distance

def findColor(degree): 
    red = 120 
    blue = 240
    green = 360
    rDif = red-degree
    rValue = abs(round(255-rDif*2.125))
    bDif = blue-degree
    bValue = abs(round(255-bDif*2.125))
    gDif = green-degree
    gValue = abs(round(255-gDif*2.125))
    values = (rValue,gValue,bValue)
    finalValues = []
    for value in values: 
        if (value > 255): 
            print (value, "is greater than 255")
            value = 0 
        finalValues += [value]
    print ("these are the values", finalValues)
    return finalValues


def rgbString(red,green,blue): 
        return "#%02x%02x%02x" % (red,green,blue)

def draw(canvas, width, height,color):
    print ("we got here")
    print (color)
    canvas.create_rectangle(10,10,110,110,fill=color)

def runDrawing(width, height,color):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height,color)
    root.mainloop()
    print("bye!")

def run(x,y): 
    angle = findAngle(x,y) 
    color = findColor(angle) 
    red = color[0]
    green = color[1]
    blue = color[2] 
    rgb = rgbString(red,green,blue)
    runDrawing(600, 600,rgb)