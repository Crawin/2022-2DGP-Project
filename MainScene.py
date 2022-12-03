import Sprite
from Define import *
from pico2d import *
import time
import math
pos = [0, 0]
textsize = [True, 154/2]         # flag, size
start = 0

mainscene = None

def enter():
    global mainscene
    mainscene = [select, home]
    pass

def draw(eTime):
    clear_canvas()
    mainscene[-1](eTime)
    update_canvas()
    pass

def home(eTime):
    background(eTime)
    text(eTime)

def select(eTime):
    pass

def background(eTime):
    global start
    if start == 0:
        start = time.time()
    global pos
    for y in range(-1, 5):
        for x in range(0, 6):
            Sprite.sprite_sheets.clip_draw(280, 170, main_pikachu_size, main_pikachu_size,
                                           pos[0] + main_pikachu_size * x, pos[1] + main_pikachu_size * y)
    pos[0] -= 78 * eTime
    pos[1] += 78 * eTime
    if pos[0] <= -main_pikachu_size:
        pos = [0, 0]

def text(eTime):
    global textsize
    Sprite.sprite_sheets.clip_draw(257, 885-879, 154, 154, 448/4, 448 - 448/4, textsize[1], textsize[1])    # 대결!
    if textsize[0]:
        textsize[1]+= 400 * eTime
        if textsize[1] >= 154:
            textsize[0] = False
    else:
        textsize[1]-= 400 * eTime
        if textsize[1] <= 154/2:
            textsize[0] = True

    Sprite.sprite_sheets.clip_draw(60,885-153,77,22,448 - 448/3,448 - (448/4 - 25))         # 포켓몬스터
    Sprite.sprite_sheets.clip_draw(53,885-663,162,34,448 - 448/3,448 - (448/4 + 25))        # 피카츄 배구
    Sprite.sprite_sheets.clip_draw(258,885-62,76,13,448/2,448/3,76*2,13*2)                  # 혼자서 재미있게

# def update(eTime):
#     draw(eTime)