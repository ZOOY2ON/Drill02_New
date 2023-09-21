#Drill02 캐릭터 사각 운동과 원 운동
# 사각형 운동과 원 운동을 번갈아 가면서 무한 반복함

from pico2d import*

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')
    pass

def run_rectangle():
    print('RECTANGLE')
    pass

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()