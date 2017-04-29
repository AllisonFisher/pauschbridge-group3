from tkinter import *
import math

# updated by Jun
# color scheme still needs discussion

def findAngle(x,y): 
    radian = math.atan2(y,x)
    degree = radian * (360/(2*math.pi))
    if (degree < 0): 
        degree = 360 + degree
    return degree


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
            
            value = 0 
        
        finalValues += [value]

    return finalValues


def rgbString(red,green,blue): 
        return "#%02x%02x%02x" % (red,green,blue)


def draw(canvas, i, color):
    size = 100
    lo = 10 + i*size
    hi = 10 + (i+1)*size
    canvas.create_rectangle(lo, lo, hi, hi,fill=color)

def runDrawing(width, height,colors):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    for i in range(len(colors)):
        draw(canvas, i, colors[i])
    root.mainloop()


def getRGB(x,y): 
    angle = findAngle(x,y) 
    color = findColor(angle) 
    red = color[0]
    green = color[1]
    blue = color[2] 
    rgb = rgbString(red,green,blue)
    return rgb
    
def run():
    points = [(1,1), (1,-1), (-1,1), (-1,-1)]
    colors = []
    for point in points:
        (x, y) = point
        rgb = getRGB(x, y)
        colors.append(rgb)
    runDrawing(600, 600,colors)



