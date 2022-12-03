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
Scene.enter('main')
frame_time = time.time()
while running:
    running = Scene.handle_events()
    elapsed_time = time.time() - frame_time
    Scene.draw(elapsed_time)
    frame_time += elapsed_time
    delay(0.01)

Scene.exit('play')
Scene.exit_running()
close_canvas()
# -----------------------------------
