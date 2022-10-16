from pico2d import *
import Player
import Sprite
import Ball
import Map
# -----------------------------------
open_canvas(448, 448)
Sprite.load_sprites()
running = True
Player.enter()
Ball.enter()
while running:
    Map.draw()
    Player.handle_events()
    Player.update()
    Ball.update()
    delay(0.01)
Ball.exit()
Player.exit()
close_canvas()
# -----------------------------------
