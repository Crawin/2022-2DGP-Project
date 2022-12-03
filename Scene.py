from pico2d import *

import Player
import Map
import Ball
import Sprite
import Events
import MainScene

SceneList= []

def handle_events():            # 키보드 입력
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_ESCAPE:
            return False
        else:
            if SceneList[-1] == 'play':
                Events.keyboard_input(event)
            elif SceneList[-1] == 'main':
                # Events.main_input(event)
                if event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_RETURN:
                    exit()
                    MainScene.mainscene.pop()
                    if len(MainScene.mainscene) == 0:
                        SceneList.pop()
                        enter('play')
                elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_RIGHT:
                    MainScene.selectpos[0]=1
                elif event.type == SDL_KEYDOWN and event.key == pico2d.SDLK_LEFT:
                    MainScene.selectpos[0]=0
    return True

def draw(eTime):
    if SceneList[-1] == 'play':
        Map.draw()
        Player.update(eTime)
        Ball.update(eTime)
    elif SceneList[-1] == 'main':
        MainScene.draw(eTime)
        # MainScene.update(eTime)
        pass

def enter(type):
    SceneList.append(type)
    match type:
        case 'play':
            Map.enter()
            Player.enter()
            Ball.enter()
            pass
        case 'main':
            MainScene.enter()
            pass

def exit():
    if SceneList[-1] == 'play':
        Ball.exit()
        Player.exit()
        Map.exit()
    elif SceneList[-1] == 'main':
        pass

def exit_running():
    pass