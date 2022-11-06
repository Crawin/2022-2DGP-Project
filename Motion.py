import time
import Sprite

class JUMP:
    def __init__(self):
        self.start_time = time.time()
        self.casting_time = 10
        self.cool_time = 0

        self.frame = [True, 1]

    def exit(self):
        self.start_time = 0

    def casting(self, pos):
        if self.jump_frame[1] == 0:
            Sprite.sprite_sheets[0].clip_draw(self.jump_frame[1] * Sprite.sprite_size,
                                   885 - (266 + Sprite.sprite_size * 2),
                                   Sprite.sprite_size, Sprite.sprite_size,
                                   pos[0], pos[1])
        else:
            Sprite.sprite_sheets[0].clip_draw((self.jump_frame[1] + 4) * Sprite.sprite_size,
                                   885 - (266 + Sprite.sprite_size),
                                   Sprite.sprite_size, Sprite.sprite_size,
                                   pos[0], pos[1])
        if self.update_frame % 5 == 0:
            if self.frame[0]:
                if self.frame[1] == 1:
                    self.frame[1] = 2
                elif self.frame[1] == 2:
                    self.frame[1] = 0
                elif self.frame[1] == 0:
                    self.frame[1] = 2
                    self.frame[0] = False
            else:
                if self.frame[1] == 0:
                    self.frame[1] = 2
                elif self.frame[1] == 2:
                    self.frame[1] = 1
                elif self.frame[1] == 1:
                    self.frame[1] = 2
                    self.frame[0] = True

class DIVE:
    pass

class SPIKE:
    pass

class IDLE:
    def __init__(self):
        self.start_time = time.time()
        self.casting_time = 0
        self.cool_time = 0

        self.frame = [True, 0]

    def exit(self):
        self.start_time = 0

    def casting(self, pos, update_frame):
        Sprite.sprite_sheets[0].clip_draw(self.frame[1] * Sprite.sprite_size,
                                          885 - (266 + Sprite.sprite_size),
                                          Sprite.sprite_size, Sprite.sprite_size,
                                          pos[0], pos[1])
        if update_frame % 10 == 0:
            if self.frame[0]:
                self.frame[1] += 1
                if self.frame[1] == 4:
                    self.frame[0] = False
            else:
                self.frame[1] -= 1
                if self.frame[1] == 0:
                    self.frame[0] = True