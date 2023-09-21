#Drill02 캐릭터 사각 운동과 원 운동
# 사각형 운동과 원 운동을 번갈아 가면서 무한 반복함

from pico2d import *
import math

open_canvas()

#grass = load_image('grass.png')
#character = load_image('character.png')

def rander_frame(x,y):
    clear_canvas_now()
    #grass.draw_now()
    #character.draw_now(x,y)
    delay(0.01)
    print(x,y)

def run_circle():

    center_x, center_y, r = 400, 300, 200

    for deg in range(0,360,5):
        x = center_x + r*math.cos(math.radians(deg))
        y = center_y + r*math.sin(math.radians(deg))

    rander_frame(x,y)


def run_rectangle():
    print('RECTANGLE')

    for x in range(50,750+1,10):
        rander_frame(x,90)

    for y in range(90,550+1,10):
        rander_frame(750,y)

    for x in range(750,50-1,-10):
        rander_frame(x,550)

    for y in range(550,90-1,-10):
        rander_frame(50,y)

def bug_check():
    for x in range(750,50-1,-10):
        print (x)

while True:

    #run_circle()
    run_rectangle()
    break

#bug_check()
close_canvas()