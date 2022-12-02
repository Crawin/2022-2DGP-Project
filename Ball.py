from pico2d import *

import Player
import Sprite
import math
import time
import random
from Define import *
# 885
# 87 157

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
BALL_SPEED_KMPH = 10 # Km / Hour
BALL_SPEED_MPM = (BALL_SPEED_KMPH * 1000.0 / 60.0)
BALL_SPEED_MPS = (BALL_SPEED_MPM / 60.0)
BALL_SPEED_PPS = (BALL_SPEED_MPS * PIXEL_PER_METER)
class C_ball:
    def __init__(self):
        self.pos = [90, 300]
        self.prepos = []
        self.frame = [0, 0]         # 매 프레임마다 1씩 증가, 5프레임마다 1씩 증가
        self.dir = [0, -1]          # 방향벡터
        self.vel = BALL_SPEED_PPS
        self.coll = ""
        self.spikeTime = 0
        self.spikePos = [0,0]

    def draw(self):
        Sprite.sprite_sheets.clip_draw((self.frame[1] * ball_size) + 87,
                                          885 - (157 + ball_size),
                                          ball_size, ball_size,
                                          self.pos[0], self.pos[1])
        self.frame[0] += 1
        if self.frame[0] % 5 == 0:
            self.frame[1] = (self.frame[1] + 1) % 5
        if time.time()-self.spikeTime < 0.5:
            Sprite.sprite_sheets.clip_draw((6 * ball_size) + 87,
                                           885 - (157 + ball_size),
                                           ball_size, ball_size,
                                           self.spikePos[0], self.spikePos[1])
        else:
            self.spikeTime= 0
        if self.coll == "spikeP1":
            Sprite.sprite_sheets.clip_draw((7 * ball_size) + 87,
                                           885 - (157 + ball_size),
                                           ball_size, ball_size,
                                           self.prepos[0], self.prepos[1])


    def move(self, eTime):
        if self.dir[1] * (self.dir[1] - 0.1) < 0:
            self.coll = ""
        self.prepos = [self.pos[0], self.pos[1]]
        self.dir[1] = self.dir[1] - 0.1
        self.pos[0] += self.dir[0] * self.vel * eTime
        self.pos[1] += self.dir[1] * self.vel * eTime
        self.collision(eTime)

    def aabb(self,rx,lx,ty,by):
        draw_rectangle(lx, by, rx, ty)
        if (self.pos[0] - ball_size / 2 > rx) or (self.pos[0] + ball_size / 2 < lx):
            return False
        if (self.pos[1] - ball_size / 2 > ty) or (self.pos[1] + ball_size / 2 < by):
            return False
        return True

    def collision(self, eTime):
        if self.pos[1] - ball_size/2 < floor:
            self.dir[1] = -self.dir[1]
            self.pos = [self.prepos[0],self.prepos[1]]
            print("gameover")
            self.coll = "floor"

        if self.pos[1]> 448:
            self.dir[1] = -self.dir[1]
            self.pos = [self.prepos[0],self.prepos[1]]
            self.coll = "top"

        if self.pos[0] - ball_size / 2 < 0 or self.pos[0] + ball_size / 2 > 448:
            self.dir[0] = -self.dir[0]
            self.pos = [self.prepos[0],self.prepos[1]]
            self.coll = "side"

        if self.coll != "bar":
            if self.aabb(230 + 8, 230 - 8, 70 + 16 * 8+8, 80 - 8):  # 기둥과 충돌
                self.coll = "bar"
                self.pos = [self.prepos[0], self.prepos[1]]
                if self.pos[0] < 230 + 8 and self.pos[0] > 230 -8 and self.pos[1] > 70 + 16 * 8+8:
                    self.dir[1] = -self.dir[1]
                elif self.pos[0] >= 230 + 8:
                    self.dir[0] = abs(self.dir[0])
                elif self.pos[0] <= 230 - 8:
                    self.dir[0] = -abs(self.dir[0])

        if Player.P1.motion == 'spike' and self.coll != "spikeP1":
            if self.aabb(Player.P1.pos[0] + sprite_size / 2,
                         Player.P1.pos[0] - sprite_size / 2 + 30,
                         Player.P1.pos[1] + sprite_size / 2 + 10,
                         Player.P1.pos[1] - sprite_size / 2 + 30):
                self.coll = "spikeP1"
                self.spikeTime = time.time()
                self.spikePos = [self.pos[0],self.pos[1]]
                self.dir = [5, -3]
                self.pos = [self.prepos[0],self.prepos[1]]
        elif Player.P1.motion == 'dive' and self.coll != "P1":
            if self.aabb(Player.P1.pos[0] + sprite_size / 2,
                         Player.P1.pos[0] - sprite_size / 2,
                         Player.P1.pos[1] + sprite_size / 2 - 30,
                         Player.P1.pos[1] - sprite_size / 2 + 30):
                self.coll = "P1"
                self.dir[1] = -self.dir[1]
                self.pos = [self.prepos[0], self.prepos[1]]
        elif self.coll != "spikeP1" and self.dir[1] < -1:
            if self.aabb(Player.P1.pos[0] + sprite_size / 2 - 10,
                         Player.P1.pos[0] - sprite_size / 2 + 30,
                         Player.P1.pos[1] + sprite_size / 2 - 10,
                         Player.P1.pos[1] - sprite_size / 2 + 50):
                self.coll = "P1"
                if self.pos[1] > (Player.P1.pos[1] + sprite_size / 2 - 10) :
                    self.dir[1] = -self.dir[1]
                    self.pos = [self.prepos[0], self.prepos[1]]
                differPos = [self.pos[0]-Player.P1.pos[0],self.pos[1]-(Player.P1.pos[1] + sprite_size / 2 - 10)]
                if differPos[0] != 0:
                    self.dir[0] = differPos[0] / abs(differPos[0])
                self.dir[1] = min(8, abs(self.dir[1] + Player.P1.dir[1]))

        if Player.P2.motion == 'spike' and self.coll != "spikeP2":
            if self.aabb(Player.P2.pos[0] + sprite_size / 2 - 30,
                         Player.P2.pos[0] - sprite_size / 2,
                         Player.P2.pos[1] + sprite_size / 2 + 10,
                         Player.P2.pos[1] - sprite_size / 2 + 30):
                self.coll = "spikeP2"
                self.spikeTime = time.time()
                self.spikePos = [self.pos[0],self.pos[1]]
                self.dir = [-5, -3]
                self.pos = [self.prepos[0],self.prepos[1]]
        elif Player.P2.motion == 'dive' and self.coll != "P2":
            if self.aabb(Player.P2.pos[0] + sprite_size / 2,
                         Player.P2.pos[0] - sprite_size / 2,
                         Player.P2.pos[1] + sprite_size / 2 - 30,
                         Player.P2.pos[1] - sprite_size / 2 + 30):
                self.coll = "P2"
                self.dir[1] = -self.dir[1]
                self.pos = [self.prepos[0], self.prepos[1]]
        elif self.coll != "spikeP2" and self.dir[1] < -1:
            if self.aabb(Player.P2.pos[0] + sprite_size / 2 - 30,
                         Player.P2.pos[0] - sprite_size / 2 + 10,
                         Player.P2.pos[1] + sprite_size / 2 - 10,
                         Player.P2.pos[1] - sprite_size / 2 + 50):
                self.coll = "P2"
                if self.pos[1] > (Player.P2.pos[1] + sprite_size / 2 - 10) :
                    self.dir[1] = -self.dir[1]
                    self.pos = [self.prepos[0], self.prepos[1]]
                differPos = [self.pos[0]-Player.P2.pos[0],self.pos[1]-(Player.P2.pos[1] + sprite_size / 2 - 10)]
                if differPos[0] != 0:
                    self.dir[0] = differPos[0] / abs(differPos[0])
                self.dir[1] = min(8, abs(self.dir[1] + Player.P2.dir[1]))


ball = None

def enter():
    global ball
    ball = C_ball()

def exit():
    global ball
    del ball

def update(eTime):
    ball.move(eTime)
    ball.draw()
    update_canvas()

