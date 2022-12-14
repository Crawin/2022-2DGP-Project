from pico2d import *

import Scene
import Sprite
from Define import *
import Ball
import math
import MainScene

PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
Move_Speed = RUN_SPEED_PPS
Move_Speed2 = RUN_SPEED_PPS

JUMP_SPEED_KMPH = 150
JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)
Jump_Speed = JUMP_SPEED_PPS

Goal_score = 7
class player:
    bgm = None
    def __init__(self, playerNum, type):
        self.score = 0
        if playerNum == 1:
            self.pos = [90, floor + sprite_size]              # x, y 위치
        elif playerNum == 2:
            self.pos = [358, floor+ sprite_size]              # x, y 위치
        self.dir = [0, 0, False]            # [+면 우측이동 -면 좌측이동, 점프 스피드, True면 눌린상태]
        self.update_frame = 0               # 입력 딜레이가 0.01이여야 조작감이 좋아서 애니메이션은 딜레이가 0.1이 되도록 하는 변수
        self.num = playerNum
        self.type = type

        self.idle_frame = [True, 0]         # True 면 프레임 +, False 면 프레임 -
        self.jump_frame = [True, 1]         # Flag, frame
        self.spike_frame = [True, 0]        # Flag, frame
        self.dive_frame = [0, 0, 0]     # head, frame, Timer
        self.gameset_frame = 0              # 264 463       132 530

        self.motion = 'idle'
        self.motion_type = {'idle': self.idle_motion, 'dive': self.dive_motion,
                            'jump': self.jump_motion, 'spike': self.spike_motion,
                            'gameset': self.gameset_motion}

        if player.bgm is None:
            player.bgm = {'motion':load_wav('Resource/Bgm/motion.wav'),'spike':load_wav('Resource/Bgm/spike.wav'), 'gameset':load_wav('Resource/Bgm/gameset.wav')}
            player.bgm['motion'].set_volume(18)
            player.bgm['spike'].set_volume(18)
            player.bgm['gameset'].set_volume(18)


    def draw(self):
        self.motion_type[self.motion]()
        if self.num == 1:
            Sprite.sprite_sheets.clip_draw(self.score * 34 + 203,
                                           885-153,
                                           34, 27,
                                           50, 400)
        elif self.num == 2:
            Sprite.sprite_sheets.clip_draw(self.score * 34 + 203,
                                           885-153,
                                           34, 27,
                                           446 - 50, 400)
        if P1.score == Goal_score or P2.score == Goal_score:        # 126 84
            Sprite.sprite_sheets.clip_draw(126,
                                           885-84,
                                           93, 17,
                                           223, 446*3/4, 93+self.update_frame, 17+self.update_frame)

    def move(self, eTime):
        global Move_Speed, Move_Speed2
        if self.type == 'PLAYER':
            # 다이브 모션 진행중이면 다이빙
            if self.motion == 'dive':
                self.pos[0] += self.dive_frame[0] * Move_Speed * eTime  # 좌우이동
                Move_Speed = max(0, Move_Speed - RUN_SPEED_PPS*2 / 50)
            else:
                self.pos[0] += self.dir[0] * Move_Speed * eTime # 좌우이동
            if self.num == 1:
                self.pos[0] = clamp((sprite_size / 2), self.pos[0], 230 - 12 - (sprite_size /2))
            elif self.num == 2:
                self.pos[0] = clamp(230 + 12 + (sprite_size / 2), self.pos[0], 433 - (sprite_size / 2))
            if self.pos[1]-sprite_size == floor and self.dir[2] and self.motion == 'idle':   # 캐릭터가 바닥에 있고, 윗키가 눌린 상태면서 idle 상태면
                self.dir[1] = Jump_Speed * eTime
            self.pos[1] += self.dir[1]        # 점프
            if self.pos[1]-sprite_size > floor:
                self.dir[1] -= 80 * eTime
            else:
                self.dir[1] = 0
                self.pos[1] = floor +sprite_size
        elif self.type == 'AI':
            u2 = Ball.ball.dir[1]
            if u2 < 0:
                x1 = Ball.ball.pos[0]
                y1 = Ball.ball.pos[1]
                u1 = Ball.ball.dir[0]
                if u1 != 0 and u2 != 0:
                    goalx = (((self.pos[1] + sprite_size / 2 - 10)-y1)*u1/u2) + x1
                    spikex = ((300-y1)*u1/u2) + x1
                    AIdirx = goalx - self.pos[0]
                    if AIdirx > 0:
                        self.dir[0] = 1
                    elif AIdirx < 0:
                        self.dir[0] = -1
                    else:
                        self.dir[0] = 0
                    if abs(self.pos[0] - goalx) > 20 and self.motion == "idle" and y1 < 200:
                        if self.num == 1:
                            if x1 < 230:
                                self.motion = 'dive'
                                player.bgm['motion'].play()
                                self.dive_frame[0] = self.dir[0]
                                Move_Speed2 = RUN_SPEED_PPS * 2
                        elif self.num == 2:
                            if x1 > 230:
                                self.motion = 'dive'
                                player.bgm['motion'].play()
                                self.dive_frame[0] = self.dir[0]
                                Move_Speed2 = RUN_SPEED_PPS * 2

                    if self.motion == 'dive':
                        self.pos[0] += self.dive_frame[0] * Move_Speed2 * eTime  # 좌우이동
                        Move_Speed2 = max(0, Move_Speed2 - RUN_SPEED_PPS * 2 / 50)
                    elif self.motion == 'idle':
                        self.pos[0] += self.dir[0] * Move_Speed2 * eTime  # 좌우이동
                    if self.num == 1:
                        self.pos[0] = clamp((sprite_size / 2), self.pos[0], 230 - 12 - (sprite_size /2))
                        spikegoalx = (300-self.pos[1])*(5)/(-3) + self.pos[0]
                    elif self.num == 2:
                        self.pos[0] = clamp(230 + 12 + (sprite_size / 2), self.pos[0], 433 - (sprite_size / 2))
                        spikegoalx = (300-self.pos[1])*(-5)/(-3) + self.pos[0]

                    if self.motion == 'idle' and (abs(self.pos[0] - spikex) < 20 or abs((self.pos[1] + sprite_size / 2 - 10) - y1) < 30):
                        self.dir[1] = Jump_Speed * eTime
                        self.dir[2] = True

                    if self.motion == 'jump' and ((self.num == 1 and spikegoalx < 230) or (self.num == 2 and spikegoalx > 238)):
                        self.motion = 'spike'
                        player.bgm['spike'].play()
            self.pos[1] += self.dir[1]  # 점프
            if self.pos[1] - sprite_size > floor:
                self.dir[1] -= 80 * eTime
            else:
                self.dir[1] = 0
                self.pos[1] = floor + sprite_size
    def idle_motion(self):
        if self.num == 1:
            Sprite.sprite_sheets.clip_draw(self.idle_frame[1] * sprite_size,
                                   885 - (266 + sprite_size),
                                   sprite_size, sprite_size,
                                   self.pos[0], self.pos[1])
        elif self.num == 2:
            Sprite.sprite_sheets.clip_composite_draw(self.idle_frame[1] * sprite_size,
                                   885 - (266 + sprite_size),
                                   sprite_size, sprite_size,0,'h',
                                       self.pos[0], self.pos[1],66,66)
        if self.update_frame % 10 == 0:
            if self.idle_frame[0]:
                self.idle_frame[1] += 1
                if self.idle_frame[1] == 4:
                    self.idle_frame[0] = False
            else:
                self.idle_frame[1] -= 1
                if self.idle_frame[1] == 0:
                    self.idle_frame[0] = True

    def jump_motion(self):
        if self.num == 1:
            if self.jump_frame[1] == 0:
                Sprite.sprite_sheets.clip_draw(self.jump_frame[1] * sprite_size,
                                       885 - (266 + sprite_size * 2),
                                       sprite_size, sprite_size,
                                       self.pos[0], self.pos[1])
            else:
                Sprite.sprite_sheets.clip_draw((self.jump_frame[1] + 4) * sprite_size,
                                       885 - (266 + sprite_size),
                                       sprite_size, sprite_size,
                                       self.pos[0], self.pos[1])
        elif self.num == 2:
            if self.jump_frame[1] == 0:
                Sprite.sprite_sheets.clip_composite_draw(self.jump_frame[1] * sprite_size,
                                       885 - (266 + sprite_size * 2),
                                       sprite_size, sprite_size,0,'h',
                                       self.pos[0], self.pos[1],66,66)
            else:
                Sprite.sprite_sheets.clip_composite_draw((self.jump_frame[1] + 4) * sprite_size,
                                       885 - (266 + sprite_size),
                                       sprite_size, sprite_size,0,'h',
                                       self.pos[0], self.pos[1],66,66)

        if self.update_frame % 5 == 0:
            if self.jump_frame[0]:
                if self.jump_frame[1] == 1:
                    self.jump_frame[1] = 2
                elif self.jump_frame[1] == 2:
                    self.jump_frame[1] = 0
                elif self.jump_frame[1] == 0:
                    self.jump_frame[1] = 2
                    self.jump_frame[0] = False
            else:
                if self.jump_frame[1] == 0:
                    self.jump_frame[1] = 2
                elif self.jump_frame[1] == 2:
                    self.jump_frame[1] = 1
                elif self.jump_frame[1] == 1:
                    self.jump_frame[1] = 2
                    self.jump_frame[0] = True

    def dive_motion(self):
        if self.num == 1:
            if self.dive_frame[0] < 0:
                Sprite.sprite_sheets.clip_composite_draw((self.dive_frame[1] + 1) * sprite_size,
                                       885 - (266 + sprite_size * 3),
                                       sprite_size, sprite_size,0,'h',
                                       self.pos[0], self.pos[1],66,66)
            else:
                Sprite.sprite_sheets.clip_draw((self.dive_frame[1] + 1) * sprite_size,
                                       885 - (266 + sprite_size * 3),
                                       sprite_size, sprite_size,
                                       self.pos[0], self.pos[1])
        elif self.num == 2:
            if self.dive_frame[0] < 0:
                Sprite.sprite_sheets.clip_composite_draw((self.dive_frame[1] + 1) * sprite_size,
                                       885 - (266 + sprite_size * 3),
                                       sprite_size, sprite_size,0,'h',
                                       self.pos[0], self.pos[1],66,66)
            else:
                Sprite.sprite_sheets.clip_draw((self.dive_frame[1] + 1) * sprite_size,
                                       885 - (266 + sprite_size * 3),
                                       sprite_size, sprite_size,
                                       self.pos[0], self.pos[1])

        if self.update_frame % 10 == 0:
            self.dive_frame[2] += 1     # 타이머 증가
            self.dive_frame[1] += 1     # 다음 프레임으로 총 3프레임
            if self.dive_frame[1] > 2:
                self.dive_frame[1] -= 1

    def spike_motion(self):
        if self.num == 1:
            Sprite.sprite_sheets.clip_draw((self.spike_frame[1] + 3) * sprite_size,
                                   885 - (266 + sprite_size * 2),
                                   sprite_size, sprite_size,
                                   self.pos[0], self.pos[1])
        elif self.num == 2:
            Sprite.sprite_sheets.clip_composite_draw((self.spike_frame[1] + 3) * sprite_size,
                                   885 - (266 + sprite_size * 2),
                                   sprite_size, sprite_size,0,'h',
                                    self.pos[0], self.pos[1],66,66)
        if self.update_frame % 5 == 0:
            if self.spike_frame[0]:
                self.spike_frame[1] += 1
                if self.spike_frame[1] == 3:
                    self.spike_frame[0] = False
            else:
                self.spike_frame[1] -= 1
                if self.spike_frame[1] == 0:
                    self.spike_frame[0] = True
                    self.motion = 'jump'

    def gameset_motion(self):
        if self.score == Goal_score:
            if self.gameset_frame <3:
                Sprite.sprite_sheets.clip_draw((self.gameset_frame + 4) * sprite_size,
                                       885 - 463,
                                       sprite_size, sprite_size,
                                       self.pos[0], self.pos[1])
            else:
                Sprite.sprite_sheets.clip_draw((self.gameset_frame - 3) * sprite_size,
                                       885 - 530,
                                       sprite_size, sprite_size,
                                       self.pos[0], self.pos[1])
        else:
            Sprite.sprite_sheets.clip_draw((self.gameset_frame + 2) * sprite_size,
                                           885 - 530,
                                           sprite_size, sprite_size,
                                           self.pos[0], self.pos[1])

        if self.update_frame % 20 == 0:
            self.gameset_frame += 1
            if self.gameset_frame > 4:
                self.gameset_frame = 4




    def update_motion(self):
        if self.motion == 'idle':
            if self.dir[2]:
                self.motion = 'jump'
                player.bgm['motion'].play()

        if self.motion == 'jump' or self.motion == 'spike':
            if self.pos[1] - sprite_size <= floor:
                self.motion = 'idle'
                self.dir[2] = False

        if self.motion == 'dive':
            if self.dive_frame[2] >= 5:     # 5프레임이 지나면 idle로 복귀
                global Move_Speed
                Move_Speed = RUN_SPEED_PPS
                self.motion = 'idle'
                self.dive_frame = [0, 0, 0]

        if (P1.score == Goal_score or P2.score == Goal_score) and self.motion != 'gameset':
            self.motion = 'gameset'
            self.dir = [0, 0, False]
            player.bgm['gameset'].play()

    def update(self, eTime):
        if self.motion != 'gameset':
            self.move(eTime)
        self.update_motion()
        self.draw()
        self.update_frame += 1

    def restart(self):
        if self.num == 1:
            self.pos = [90, floor + sprite_size]  # x, y 위치
        elif self.num == 2:
            self.pos = [358, floor + sprite_size]  # x, y 위치
        self.update_frame = 0  # 입력 딜레이가 0.01이여야 조작감이 좋아서 애니메이션은 딜레이가 0.1이 되도록 하는 변수

        self.idle_frame = [True, 0]  # True 면 프레임 +, False 면 프레임 -
        self.jump_frame = [True, 1]  # Flag, frame
        self.spike_frame = [True, 0]  # Flag, frame
        self.dive_frame = [0, 0, 0]  # head, frame, Timer
        self.motion = 'idle'



P1 = None
P2 = None
def enter():
    global P1
    global P2
    if MainScene.selectpos[0] == 0:
        P1 = player(1, 'PLAYER')
        P2 = player(2, 'AI')
    elif MainScene.selectpos[0] == 1:
        P1 = player(1, 'AI')
        P2 = player(2, 'PLAYER')

def exit():
    global P1
    del P1
    global P2
    del P2

def update(eTime):
    P1.update(eTime)
    P2.update(eTime)

def restart():
    P1.restart()
    P2.restart()
