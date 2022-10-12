from pico2d import *
import Player
import Sprite
Jump_Speed = 20

def handle_events():
    global running
    global P1
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                P1.dir[0] += 1
            elif event.key == SDLK_LEFT:
                P1.dir[0] -= 1
            elif event.key == SDLK_UP:
                if P1.pos[1] == 90:
                    P1.dir[1] = Jump_Speed
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                P1.dir[0] -= 1
            elif event.key == SDLK_LEFT:
                P1.dir[0] += 1
    pass

open_canvas()

Sprite.load_sprites()

running = True
P1 = Player.character()

while running:
    clear_canvas()

    P1.update()

    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()

