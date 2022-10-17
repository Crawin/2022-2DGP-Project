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
# Map.enter()
# Player.enter()
# Ball.enter()
while running:
    Scene.handle_events('play')
    Scene.draw('play')
    # Map.draw()
    # # Player.handle_events()
    # Player.update()
    # Ball.update()
    delay(0.01)

Scene.exit()
# Ball.exit()
# Player.exit()
# Map.exit()
close_canvas()
# -----------------------------------
