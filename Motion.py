import time

class JUMP:
    def __init__(self):
        self.start_time = time.time()
        self.casting_time = 10
        self.cool_time = 0

        self.frame = [True, 1]

    def exit(self):
        self.start_time = 0

    def getStarttime(self):
        return self.start_time

    def casting(self):
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
    pass
