from pico2d import *

sprite_sheets = [None, None]
sprite_size = 66
ball_size = 42
def load_sprites():
    global sprite_sheets
    sprite_sheets = [load_image('Resource/Image/sprite_sheet.png'), load_image('Resource/Image/sprite_sheet_reverse.png')]
