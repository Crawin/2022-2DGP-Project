from pico2d import *
Jump_Speed = 20
class Player:
    def __init__(self):
        self.pos = [90, 90]   # x, y 위치
        self.frame = 0
        self.update_frame = 0   # 입력 딜레이가 0.01이여야 조작감이 좋아서 애니메이션은 딜레이가 0.1이 되도록 하는 변수
        self.frame_flag = True  # True 면 프레임 +, False 면 프레임 -
        self.jump_frame = 1
        self.jump_frame_flag = True
        self.sprite_size = 66
        self.dir = [0, 0]            # [+면 우측이동 -면 좌측이동, 점프 스피드]
        self.enter_flag = False

    def draw(self):
        if self.pos[1] == 90:
            if self.enter_flag:
                self.dive_motion()
            else:
                self.idle_motion()
        else:
            if self.enter_flag:
                self.spike_motion()
            else:
                self.jump_motion()

    def move(self):
        self.pos[0] += self.dir[0] * 5      # 좌우이동
        self.pos[1] += self.dir[1]          # 점프
        if self.pos[1] > 90:
            self.dir[1] -= 1
        else:
            self.dir[1] = 0
            self.pos[1] = 90

    def jump_motion(self):
        if self.jump_frame == 0:
            sprite_sheet.clip_draw(self.jump_frame * self.sprite_size,
                                   885 - (266 + self.sprite_size * 2),
                                   self.sprite_size, self.sprite_size,
                                   self.pos[0], self.pos[1])
        else:
            sprite_sheet.clip_draw((self.jump_frame + 4) * self.sprite_size,
                                   885 - (266 + self.sprite_size),
                                   self.sprite_size, self.sprite_size,
                                   self.pos[0], self.pos[1])

        if self.update_frame % 5 == 0:
            if self.jump_frame_flag:
                if self.jump_frame == 1:
                    self.jump_frame = 2
                elif self.jump_frame == 2:
                    self.jump_frame = 0
                elif self.jump_frame == 0:
                    self.jump_frame = 2
                    self.jump_frame_flag = False
            else:
                if self.jump_frame == 0:
                    self.jump_frame = 2
                elif self.jump_frame == 2:
                    self.jump_frame = 1
                elif self.jump_frame == 1:
                    self.jump_frame = 2
                    self.jump_frame_flag = True

    def idle_motion(self):
        sprite_sheet.clip_draw(self.frame * self.sprite_size,
                               885 - (266 + self.sprite_size),
                               self.sprite_size, self.sprite_size,
                               self.pos[0], self.pos[1])
        if self.update_frame % 10 == 0:
            if self.frame_flag:
                self.frame += 1
                if self.frame == 4:
                    self.frame_flag = False
            else:
                self.frame -= 1
                if self.frame == 0:
                    self.frame_flag = True

    def dive_motion(self):
        pass

    def spike_motion(self):
        pass

    def update(self):
        self.update_frame += 1
        self.draw()
        self.move()



def handle_events():
    global running
    global P1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                P1.dir[0] += 1
            elif event.key == SDLK_LEFT:
                P1.dir[0] -= 1
            elif event.key == SDLK_UP:
                if P1.pos[1] == 90:
                    P1.dir[1] = Jump_Speed
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                P1.dir[0] -= 1
            elif event.key == SDLK_LEFT:
                P1.dir[0] += 1

    pass

open_canvas()
sprite_sheet = load_image('Resource/Image/sprite_sheet.png')
reverse_sprite = load_image('Resource/Image/sprite_sheet_reverse.png')

running = True
P1 = Player()

while running:
    clear_canvas()

    P1.update()

    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()

