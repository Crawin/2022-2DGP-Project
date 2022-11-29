from pico2d import *
import Player
import Sprite
import Ball
import Map
import Scene
import time
# -----------------------------------
open_canvas(448, 448)
Sprite.load_sprites()
running = True
Scene.enter('play')
frame_time = time.time()
while running:
    running = Scene.handle_events('play')
    elapsed_time = time.time() - frame_time
    Scene.draw('play', elapsed_time)
    frame_time += elapsed_time
    delay(0.01)

Scene.exit('play')
close_canvas()
# -----------------------------------
