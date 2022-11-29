from pico2d import *

import Player
import Map
import Ball
import Sprite
import Events


def handle_events(type):            # 키보드 입력
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            return False
        else:
            Events.keyboard_input(event)
    return True


    # match type:
    #     case 'play':
    #         return Events.keyboard_input()
    #         pass
    #     case 'main':
    #         pass
    # return True

def draw(type, eTime):
    match type:
        case 'play':
            Map.draw()
            Player.update(eTime)
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