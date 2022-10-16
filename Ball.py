from pico2d import *
import Sprite
# 885
# 87 157
class C_ball:
    def __init__(self):
        self.pos = [90, 300]
        self.frame = [0, 0]         # 매 프레임마다 1씩 증가, 10프레임마다 1씩 증가

    def draw(self):
        Sprite.sprite_sheets[0].clip_draw((self.frame[1] * Sprite.ball_size) + 87,
                                          885 - (157 + Sprite.ball_size),
                                          Sprite.ball_size, Sprite.ball_size,
                                          self.pos[0], self.pos[1])
        self.frame[0] += 1
        if self.frame[0] % 5 == 0:
            self.frame[1] = (self.frame[1] + 1) % 5
ball = None

def enter():
    global ball
    ball = C_ball()

def exit():
    global ball
    del ball

def update():
    ball.draw()
    update_canvas()