from pico2d import *

import Player
import Sprite
import math
# 885
# 87 157
floor = 113 - Sprite.sprite_size
class C_ball:
    def __init__(self):
        self.pos = [90, 300]
        self.frame = [0, 0]         # 매 프레임마다 1씩 증가, 10프레임마다 1씩 증가
        self.dir = [1, 0]
        self.vel = 1

    def draw(self):
        Sprite.sprite_sheets[0].clip_draw((self.frame[1] * Sprite.ball_size) + 87,
                                          885 - (157 + Sprite.ball_size),
                                          Sprite.ball_size, Sprite.ball_size,
                                          self.pos[0], self.pos[1])
        self.frame[0] += 1
        if self.frame[0] % 5 == 0:
            self.frame[1] = (self.frame[1] + 1) % 5

    def move(self):
        self.pos[0] += self.dir[0] * self.vel
        self.pos[1] += self.dir[1] * self.vel

    def collision(self):
        if self.vel < 0:
            self.dir[1] = -1
        if self.pos[1] - Sprite.ball_size < floor:
            self.dir[1] = -self.dir[1]
        if self.dir[1] < 0:
            self.vel += 0.1
        else:
            self.vel -= 0.1

        if self.pos[0] - Sprite.ball_size / 2 < 0 or self.pos[0] + Sprite.ball_size / 2 > 448:
            self.dir[0] = -self.dir[0]
ball = None

def enter():
    global ball
    ball = C_ball()

def exit():
    global ball
    del ball

def update():
    ball.collision()
    ball.move()
    ball.draw()
    update_canvas()