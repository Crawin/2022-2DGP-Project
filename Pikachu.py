from pico2d import *

def handle_events():
    # fill here
    pass

open_canvas()
sprite_sheet = load_image('Resource/Image/sprite_sheet.png')

running = True

class Player:
    def __init__(self):
        self.pos = [90, 90]   # x, y 위치
        self.frame = 0
        self.frame_flag = True  # True 면 프레임 +, False 면 프레임 -
        self.sprite_size = 66
    def draw(self):
        sprite_sheet.clip_draw(self.frame * self.sprite_size,
                               885 - (266+self.sprite_size),
                               self.sprite_size, self.sprite_size,
                               self.pos[0], self.pos[1])
    def update(self):
        self.draw()
        if self.frame_flag:
            self.frame += 1
            if self.frame == 4:
                self.frame_flag = False
        else:
            self.frame -= 1
            if self.frame == 0:
                self.frame_flag = True

P1 = Player()

while running:
    clear_canvas()

    P1.update()


    update_canvas()
    handle_events()
    delay(0.1)

close_canvas()

