from pico2d import *
import Sprite

Jump_Speed = 20
floor = 113 - 8
class player:
    def __init__(self):
        self.pos = [90, floor]                 # x, y 위치
        self.update_frame = 0               # 입력 딜레이가 0.01이여야 조작감이 좋아서 애니메이션은 딜레이가 0.1이 되도록 하는 변수
        self.idle_frame = [True, 0]         # True 면 프레임 +, False 면 프레임 -
        self.jump_frame = [True, 1]         # Flag, frame
        self.dir = [0, 0, False]            # [+면 우측이동 -면 좌측이동, 점프 스피드, True면 눌린상태]
        self.spike_frame = [True, 0]        # Flag, frame
        self.dive_frame = [0, 0]            # frame, Timer
        self.Ldive_frame = [2, 0]            # frame, Timer
        self.motion = 'idle'
        self.motion_type = {'idle': self.idle_motion, 'dive': self.dive_motion, 'Ldive': self.Ldive_motion,
                            'jump': self.jump_motion, 'spike': self.spike_motion}

    def draw(self):
        self.motion_type[self.motion]()

    def move(self):
        self.pos[0] += self.dir[0] * 5      # 좌우이동
        if self.pos[0] - (Sprite.sprite_size / 2) < 0:          # 좌측 벽 충동
            self.pos[0] = (Sprite.sprite_size / 2)
        if self.pos[0] + (Sprite.sprite_size /2) > 230 - 12:    # 우측 기둥 충돌
            self.pos[0] = 230 - 12 - (Sprite.sprite_size /2)

        if self.pos[1] == floor and self.dir[2]:   # 캐릭터가 바닥에 있고, 윗키가 눌린 상태면
            self.dir[1] = Jump_Speed
        self.pos[1] += self.dir[1]          # 점프
        if self.pos[1] > floor:
            self.dir[1] -= 1
        else:
            self.dir[1] = 0
            self.pos[1] = floor

    def idle_motion(self):
        Sprite.sprite_sheets[0].clip_draw(self.idle_frame[1] * Sprite.sprite_size,
                               885 - (266 + Sprite.sprite_size),
                               Sprite.sprite_size, Sprite.sprite_size,
                               self.pos[0], self.pos[1])
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
        if self.jump_frame[1] == 0:
            Sprite.sprite_sheets[0].clip_draw(self.jump_frame[1] * Sprite.sprite_size,
                                   885 - (266 + Sprite.sprite_size * 2),
                                   Sprite.sprite_size, Sprite.sprite_size,
                                   self.pos[0], self.pos[1])
        else:
            Sprite.sprite_sheets[0].clip_draw((self.jump_frame[1] + 4) * Sprite.sprite_size,
                                   885 - (266 + Sprite.sprite_size),
                                   Sprite.sprite_size, Sprite.sprite_size,
                                   self.pos[0], self.pos[1])

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
        Sprite.sprite_sheets[0].clip_draw((self.dive_frame[0] + 1) * Sprite.sprite_size,
                               885 - (266 + Sprite.sprite_size * 3),
                               Sprite.sprite_size, Sprite.sprite_size,
                               self.pos[0], self.pos[1])
        if self.update_frame % 10 == 0:
            self.pos[0] += 25
            if self.pos[0] - (Sprite.sprite_size / 2) < 0:
                self.pos[0] = (Sprite.sprite_size / 2)
            if self.pos[0] + (Sprite.sprite_size / 2) > 230 - 12:
                self.pos[0] = 230 - 12 - (Sprite.sprite_size / 2)
            self.dive_frame[1] += 1     # 타이머 증가
            self.dive_frame[0] += 1     # 다음 프레임으로
            if self.dive_frame[0] > 2:
                self.dive_frame[0] -= 1

    def Ldive_motion(self):
        Sprite.sprite_sheets[1].clip_draw(476 - (self.Ldive_frame[0] + 2) * Sprite.sprite_size,
                               885 - (266 + Sprite.sprite_size * 3),
                               Sprite.sprite_size, Sprite.sprite_size,
                               self.pos[0], self.pos[1])
        if self.update_frame % 10 == 0:
            self.pos[0] -= 25
            if self.pos[0] - (Sprite.sprite_size / 2) < 0:
                self.pos[0] = (Sprite.sprite_size / 2)
            if self.pos[0] + (Sprite.sprite_size / 2) > 230 - 12:
                self.pos[0] = 230 - 12 - (Sprite.sprite_size / 2)
            self.Ldive_frame[1] += 1     # 타이머 증가
            self.Ldive_frame[0] += 1     # 다음 프레임으로
            if self.Ldive_frame[0] > 2:
                self.Ldive_frame[0] -= 1

    def spike_motion(self):
        Sprite.sprite_sheets[0].clip_draw((self.spike_frame[1] + 3) * Sprite.sprite_size,
                               885 - (266 + Sprite.sprite_size * 2),
                               Sprite.sprite_size, Sprite.sprite_size,
                               self.pos[0], self.pos[1])
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

    def update_motion(self):
        if self.motion == 'jump':
            if self.pos[1] <= floor:
                self.motion = 'idle'
        if self.dir[2] and self.motion != 'dive' and self.motion != 'Ldive' and self.motion != 'spike':
            self.motion = 'jump'
        if self.motion == 'dive':
            if self.dive_frame[1] >= 5:
                self.motion = 'idle'
                self.dive_frame[0] = 0
                self.dive_frame[1] = 0
        if self.motion == 'Ldive':
            if self.Ldive_frame[1] >= 5:
                self.motion = 'idle'
                self.Ldive_frame[0] = 0
                self.Ldive_frame[1] = 0

    def update(self):
        if self.motion != 'dive' and self.motion != 'Ldive':
            self.move()
        self.draw()
        self.update_motion()
        self.update_frame += 1
        print(self.dir)

P1 = None
P2 = None
def enter():
    global P1
    P1 = player()

def exit():
    global P1
    del P1

def update():
    P1.update()
