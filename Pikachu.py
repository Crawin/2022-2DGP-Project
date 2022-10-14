from pico2d import *
import Player
import Sprite


# -----------------------------------
open_canvas()
Sprite.load_sprites()
running = True
Player.enter()
while running:
    Player.handle_events()
    Player.update()
    delay(0.01)
Player.exit()
close_canvas()
# -----------------------------------
