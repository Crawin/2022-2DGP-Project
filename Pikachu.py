from pico2d import *
import Player
import Sprite
import Ball
import Map
import Scene

# -----------------------------------
open_canvas(448, 448)
Sprite.load_sprites()
running = True
Scene.enter('play')
while running:
    running = Scene.handle_events('play')
    Scene.draw('play')
    delay(0.01)

Scene.exit('play')
close_canvas()
# -----------------------------------
