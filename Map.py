from pico2d import *
import Sprite
from random import randint
# 2, 263 , 434,199
# 맵 크기 = 448 x 448
# 맵 타일 크기 16 x 16
# 산 크기
# 네트 크기 6 x 8
# 구름 크기 45 x 20

class cloud:
    def __init__(self):
        self.pos = [randint(0, 448), randint(448 / 2, 448 - 32)]
        self.speed = randint(1, 2)
    def move(self):
        self.pos[0] = self.pos[0] + self.speed
        if self.pos[0] - (45 / 2) >= 448:       # 구름이 맵 밖으로 나가면
            self.reset()

    def reset(self):
        self.pos = [0, randint(448 / 2, 448 - 32)]
        self.speed = randint(1, 2)

clouds = None
def enter():
    global clouds
    clouds = [cloud() for i in range(0, 10)]

def exit():
    global clouds
    for cloud in clouds:
        del cloud
    del clouds

def draw():
    clear_canvas()
    for y in range(16, 432 + 1, 32):
        for x in range(16, 432 + 1, 32):
            Sprite.sprite_sheets.clip_draw(138, 885 - 18, 16, 16, x, y, 32, 32)      # 해안가

    Sprite.sprite_sheets.clip_draw(84, 885 - 18, 16, 16, 16, 16 + 32 * 2, 32, 32)  # 바닥 선 /
    for i in range(1, 13):
        Sprite.sprite_sheets.clip_draw(66, 885 - 18, 16, 16, 16 + 32 * i, 16 + 32 * 2, 32, 32)  # 바닥 선 =
    Sprite.sprite_sheets.clip_draw(102, 885 - 18, 16, 16, 432, 16 + 32 * 2, 32, 32)  # 바닥 선 \

    for x in range(16, 432 + 1, 32):
        Sprite.sprite_sheets.clip_draw(120, 885 - 18, 16, 16, x, 16 + 32 * 3, 32, 32)  # 빨간선

    Sprite.sprite_sheets.clip_draw(2, 885 - 264, 434 - 2, 263 - 199, 448 / 2, 32 * 5, 449, 64)       # 산

    for y in range(208, 432 + 1, 32):
        for x in range(16, 432 + 1, 32):
            Sprite.sprite_sheets.clip_draw(156, 885 - 18, 16, 16, x, y, 32, 32)      # 하늘

    for i in range(0, 8):
        Sprite.sprite_sheets.clip_draw(13, 885 - 10, 6, 8, 230, 70 + 16 * i, 12, 16)  # 네트 기둥
    Sprite.sprite_sheets.clip_draw(22, 885 - 10, 8, 8, 230, 70 + 16 * 8, 16, 16)  # 네트 봉

    for cloud in clouds:
        Sprite.sprite_sheets.clip_draw(101, 885 - (109+1), 45, 20, cloud.pos[0], cloud.pos[1])
        cloud.move()