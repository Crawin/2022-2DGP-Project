import Sprite
from Define import *
from pico2d import *
import time
import math
pos = [0, 0]
textsize = [True, 154/2]         # flag, size
start = 0

selectpos = [0, [True,66], [True,66]]             # 왼쪽진영, [왼쪽 flag,왼쪽 사이즈], [오른쪽flag,오른쪽사이즈]
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
    background(eTime)
    character(eTime)
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

def character(eTime):
    if selectpos[0] == 0:
        selectpos[2] = [True, 66]
        if selectpos[1][0]:
            selectpos[1][1] += 200 * eTime
            if selectpos[1][1] >= 132:
                selectpos[1][0] = False
        else:
            selectpos[1][1] -= 200 * eTime
            if selectpos[1][1] <= 66:
                selectpos[1][0] = True
    elif selectpos[0] == 1:
        selectpos[1] = [True, 66]
        if selectpos[2][0]:
            selectpos[2][1] += 200 * eTime
            if selectpos[2][1] >= 132:
                selectpos[2][0] = False
        else:
            selectpos[2][1] -= 200 * eTime
            if selectpos[2][1] <= 66:
                selectpos[2][0] = True
    Sprite.sprite_sheets.clip_draw(0, 885 - (266 + sprite_size),
                                             sprite_size, sprite_size,
                                             448/4, 224, selectpos[1][1], selectpos[1][1])
    Sprite.sprite_sheets.clip_composite_draw(0, 885 - (266 + sprite_size),
                                             sprite_size, sprite_size, 0, 'h',
                                             448/4 * 3, 224, selectpos[2][1], selectpos[2][1])