from colorama import Fore, Back, Style
import turtle
from PIL import Image
from PIL.ImageFilter import BLUR
from time import sleep
import canvasvg
outputWidth = 45
outputHeight = 45
sizeMult = 20
scaleFactor = 4


file = '/home/jimmy/Desktop/Taj-Mahal-Agra-India.jpg'
fileName = 'out'
img = Image.open(file)
img = img.resize((outputWidth,outputHeight))
width, height = img.size
print(img.mode)
#img.show()

screen = turtle.Screen()
screen.setup(width = outputWidth*sizeMult, height = outputHeight*sizeMult, startx = 2500)
screen.bgcolor("black")
screen.title("Turtle")
tur =  turtle.Turtle()
tur.penup()
tur.hideturtle()
tur.speed(0)
tur._delay(0)
#tur._tracer(0, 0)
offset=0
for i in range(0, width):
    if(offset>0):
        offset = 0
    else:
        offset = sizeMult/2
    for j in range(0, height):
        #ur.setpos(sizeMult*j-500, 450-sizeMult*i)
        tur.setpos((sizeMult/2)*j-200, 200-(sizeMult/2)*i)
        #tur.setpos((sizeMult/2)*j-200 + offset, 200-(sizeMult/2)*i)
        color = img.getpixel((j, i))
        tur.dot(sizeMult, '#{:02x}{:02x}{:02x}'.format(*color))
        #sleep(0.1)
#tur._update()
tur.getscreen().getcanvas().postscript(file= fileName+'.eps')
img3 = Image.open(fileName + '.eps') 
img3.save(fileName + '.jpg')  
turtle.done()

