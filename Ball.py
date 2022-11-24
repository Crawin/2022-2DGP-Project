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
        self.dir = [0, -1]          # 방향벡터
        self.colldir = [0, 1]       # 충돌시 방향벡터
        self.vel = 1
        # self.coll = False

    def draw(self):
        Sprite.sprite_sheets[0].clip_draw((self.frame[1] * Sprite.ball_size) + 87,
                                          885 - (157 + Sprite.ball_size),
                                          Sprite.ball_size, Sprite.ball_size,
                                          self.pos[0], self.pos[1])
        self.frame[0] += 1
        if self.frame[0] % 5 == 0:
            self.frame[1] = (self.frame[1] + 1) % 5


    def move(self):
        # if self.dir[1] * (self.dir[1] - 0.1) < 0:
        #     self.coll = False
        self.dir[1] = self.dir[1] - 0.1
        self.pos[0] += self.dir[0] * self.vel
        self.pos[1] += self.dir[1] * self.vel
        self.collision()

    def aabb(self,rx,lx,ty,by):
        draw_rectangle(lx, by, rx, ty)
        if (self.pos[0] - Sprite.ball_size / 2 > rx) or (self.pos[0] + Sprite.ball_size / 2 < lx):
            return False
        if (self.pos[1] - Sprite.ball_size / 2 > ty) or (self.pos[1] + Sprite.ball_size / 2 < by):
            return False
        return True

    def collision(self):
        if self.pos[1] - Sprite.ball_size < floor:
            self.dir[1] = -self.dir[1]
            self.pos[1] += self.dir[1] * self.vel
            print("gameover")
            # self.coll = False

        if self.pos[1] + Sprite.ball_size > 448:
            self.dir[1] = -self.dir[1]
            self.pos[1] += self.dir[1] * self.vel
            # self.coll = False

        if self.pos[0] - Sprite.ball_size / 2 < 0 or self.pos[0] + Sprite.ball_size / 2 > 448:
            self.dir[0] = -self.dir[0]
            self.pos[0] += self.dir[0] * self.vel
            # self.coll = False

        if self.aabb(230 + 8, 230 - 8, 70 + 16 * 8+8, 80 - 8):
            if self.pos[1] >= 70 + 16 * 8+8 or (self.pos[0] <= 230 + 8 and self.pos[0] >= 230 - 8):
                self.dir[1] = -self.dir[1]
                self.pos[1] += self.dir[1] * self.vel
            else:
                self.dir[0] = -self.dir[0]
                self.pos[0] += self.dir[0] * self.vel
            # self.coll = False

        if self.aabb(Player.P1.pos[0] + Sprite.sprite_size / 2 - 10,Player.P1.pos[0] - Sprite.sprite_size / 2 + 30,
                     Player.P1.pos[1] + Sprite.sprite_size / 2 - 10,Player.P1.pos[1] - Sprite.sprite_size / 2 + 50):
            if self.pos[1] > (Player.P1.pos[1] + Sprite.sprite_size / 2 - 10) and self.dir[1] <= 0:
                self.dir[1] = -self.dir[1]
                self.pos[1] += self.dir[1] * self.vel
            self.dir[0] = min(10, self.dir[0] + Player.P1.dir[0])
            self.dir[1] = min(10, self.dir[1] + Player.P1.dir[1])

ball = None

def enter():
    global ball
    ball = C_ball()

def exit():
    global ball
    del ball

def update():
    ball.move()
    ball.draw()
    update_canvas()

