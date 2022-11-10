import time
import Sprite

class JUMP:
    def __init__(self):
        print("JUMP ENTER")
        self.start_time = time.time()
        self.casting_time = 3
        self.cool_time = 0

    def enter(self):
        print("JUMP ENTER")
        self.frame = [True, 1]


    def exit(self):
        print("JUMP EXIT")
        self.start_time = 0

    def casting(self, pos, update_frame):
        if time.time() - self.start_time < self.casting_time:
            if self.frame[1] == 0:
                Sprite.sprite_sheets[0].clip_draw(self.frame[1] * Sprite.sprite_size,
                                       885 - (266 + Sprite.sprite_size * 2),
                                       Sprite.sprite_size, Sprite.sprite_size,
                                       pos[0], pos[1])
            else:
                Sprite.sprite_sheets[0].clip_draw((self.frame[1] + 4) * Sprite.sprite_size,
                                       885 - (266 + Sprite.sprite_size),
                                       Sprite.sprite_size, Sprite.sprite_size,
                                       pos[0], pos[1])
            if update_frame % 5 == 0:
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
        else:
            print("Finish Jump")
            self.exit()

class DIVE:
    pass

class SPIKE:
    pass

class IDLE:
    def __init__(self):
        print("IDLE ENTER")
        self.start_time = time.time()
        self.casting_time = 0
        self.cool_time = 0
        self.doing = False

    def enter(self):
        if self.doing:
            self.casting()
        else:
            print("IDLE ENTER")
            self.frame = [True, 0]
            self.doing = True

    def exit(self):
        print("IDLE EXIT")
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

motions = None
def load_motions():
    global motions
    motions = {'Jump': JUMP(), 'Idle': IDLE(), 'Spike': SPIKE(), 'Dive': DIVE()}

def del_motions():
    global motions
    del motions

def draw_motion(motion, pos, updatetime):
    motions[motion].enter()