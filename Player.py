from pico2d import *
import Sprite

Jump_Speed = 20

class player:
    def __init__(self):
        self.pos = [90, 90]   # x, y 위치
        self.update_frame = 0   # 입력 딜레이가 0.01이여야 조작감이 좋아서 애니메이션은 딜레이가 0.1이 되도록 하는 변수
        self.idle_frame = [True, 0]  # True 면 프레임 +, False 면 프레임 -
        self.jump_frame = [True, 1] # Flag, frame
        self.sprite_size = 66
        self.dir = [0, 0, False]            # [+면 우측이동 -면 좌측이동, 점프 스피드, True면 눌린상태]
        self.spike_frame = [True, 0]
        self.motion = 'idle'
        self.motion_type = {'idle': self.idle_motion, 'dive': self.dive_motion, 'jump': self.jump_motion, 'spike': self.spike_motion}

    def draw(self):
        self.motion_type[self.motion]()
        if self.pos[1] == 90:
            self.motion = 'idle'
        if self.dir[2]:
            self.motion = 'jump'
        # if self.pos[1] == 90:
        #     if self.motion_flag:
        #         # self.dive_motion()
        #         self.idle_motion()
        #     else:
        #         self.idle_motion()
        # else:
        #     if self.motion_flag:
        #         self.spike_motion()
        #     else:
        #         self.jump_motion()

    def move(self):
        self.pos[0] += self.dir[0] * 5      # 좌우이동
        if self.pos[1] == 90 and self.dir[2]:   # 캐릭터가 바닥에 있고, 윗키가 눌린 상태면
            self.dir[1] = Jump_Speed
        self.pos[1] += self.dir[1]          # 점프
        if self.pos[1] > 90:
            self.dir[1] -= 1
        else:
            self.dir[1] = 0
            self.pos[1] = 90

    def jump_motion(self):
        if self.jump_frame[1] == 0:
            Sprite.sprite_sheets[0].clip_draw(self.jump_frame[1] * self.sprite_size,
                                   885 - (266 + self.sprite_size * 2),
                                   self.sprite_size, self.sprite_size,
                                   self.pos[0], self.pos[1])
        else:
            Sprite.sprite_sheets[0].clip_draw((self.jump_frame[1] + 4) * self.sprite_size,
                                   885 - (266 + self.sprite_size),
                                   self.sprite_size, self.sprite_size,
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

    def idle_motion(self):
        Sprite.sprite_sheets[0].clip_draw(self.idle_frame[1] * self.sprite_size,
                               885 - (266 + self.sprite_size),
                               self.sprite_size, self.sprite_size,
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

    def dive_motion(self):
        pass

    def spike_motion(self):
        Sprite.sprite_sheets[0].clip_draw((self.spike_frame[1] + 3) * self.sprite_size,
                               885 - (266 + self.sprite_size * 2),
                               self.sprite_size, self.sprite_size,
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
        if self.pos[1] <= 110:
            self.motion = 'jump'

    def update(self):
        self.move()
        self.draw()
        self.update_frame += 1


P1 = None


def enter():
    global P1
    P1 = player()

def exit():
    global P1
    del P1

def handle_events():
    global running
    global P1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_g:
                    P1.dir[0] += 1
                elif event.key == SDLK_d:
                    P1.dir[0] -= 1
                elif event.key == SDLK_r:
                    if P1.pos[1] == 90:
                        P1.dir[2] = True
                        P1.motion = 'jump'
                        # P1.dir[1] = Jump_Speed
                elif event.key == SDLK_z:
                    if P1.motion == 'idle':
                        P1.motion = 'dive'
                    elif P1.motion == 'jump':
                        P1.motion = 'spike'
                    # if P1.pos[1] == 90:
                    #     P1.motion = 'dive'
                    # else:
                    #     P1.motion = 'spike'
                    # P1.motion_flag = True
                elif event.key == SDLK_ESCAPE:
                    running = False
        elif event.type == SDL_KEYUP:
                if event.key == SDLK_g:
                    P1.dir[0] -= 1
                elif event.key == SDLK_d:
                    P1.dir[0] += 1
                elif event.key == SDLK_r:
                    P1.dir[2] = False

    pass

def update():
    clear_canvas()
    P1.update()
    update_canvas()