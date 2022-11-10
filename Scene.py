from pico2d import *
import Player
import Map
import Player
import Ball
import Sprite
import Motion

def handle_events(type):            # 키보드 입력
    match type:
        case 'play':
            events = get_events()
            for event in events:
                if event.type == SDL_KEYDOWN:
                    match event.key:
                        case pico2d.SDLK_g:
                            Player.P1.dir[0] += 1
                        case pico2d.SDLK_d:
                            Player.P1.dir[0] -= 1
                        case pico2d.SDLK_r:
                            if Player.P1.pos[1] == Player.floor:
                                if Player.P1.motion != 'dive' and Player.P1.motion != 'Ldive':
                                    Player.P1.motion = 'jump'
                                    Player.P1.motion2.exit()
                                    Player.P1.motion2 = Motion.JUMP()

                            Player.P1.dir[2] = True
                        case pico2d.SDLK_z:
                            if Player.P1.motion == 'idle':
                                if Player.P1.dir[0] == -1:
                                    Player.P1.motion = 'Ldive'
                                else:
                                    Player.P1.motion = 'dive'
                            elif Player.P1.motion == 'jump':
                                Player.P1.motion = 'spike'
                        case pico2d.SDLK_ESCAPE:
                            pass
                elif event.type == SDL_KEYUP:
                    match event.key:
                        case pico2d.SDLK_g:
                            Player.P1.dir[0] -= 1
                        case pico2d.SDLK_d:
                            Player.P1.dir[0] += 1
                        case pico2d.SDLK_r:
                            Player.P1.dir[2] = False
            pass
        case 'main':
            pass

def draw(type):
    match type:
        case 'play':
            Map.draw()
            Player.update()
            Ball.update()
        case 'main':
            pass

def enter(type):
    match type:
        case 'play':
            Map.enter()
            Player.enter()
            Ball.enter()
            pass
        case 'main':
            pass

def exit(type):
    match type:
        case 'play':
            Ball.exit()
            Player.exit()
            Map.exit()
        case 'main':
            pass