from turtle import *
import time

colors = ['blue', 'purple', 'pink']
bgcolor("black")
pensize(3)
speed(50)
down()
i = 0

for radius in range(0, 1000):
    forward(radius)
    left(45)
    if i >= len(colors):
        i -= len(colors)
    else:
        i += 1
    pencolor('white')
    
time.sleep(5)
