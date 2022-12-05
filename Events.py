import pico2d
from pico2d import *
import Player
import MainScene

def keyboard_input(event):
    if MainScene.selectpos[0] == 0:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_g:             # 우측 이동
                    Player.P1.dir[0] += 1
                case pico2d.SDLK_d:             # 좌측 이동
                    Player.P1.dir[0] -= 1
                case pico2d.SDLK_r:
                    Player.P1.dir[2] = True
                case pico2d.SDLK_z:
                    if Player.P1.motion == 'idle':
                        Player.P1.motion = 'dive'
                        Player.player.bgm['motion'].play()
                        Player.Move_Speed = Player.RUN_SPEED_PPS * 2
                        if Player.P1.dir[0] < 0:
                            Player.P1.dive_frame[0] = -1            # z키를 눌렀을때 어디 방향을 보고 있는지 입력
                        else:
                            Player.P1.dive_frame[0] = 1
                    elif Player.P1.motion == 'jump':
                        Player.P1.motion = 'spike'
                        Player.player.bgm['spike'].play()

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_g:
                    Player.P1.dir[0] -= 1
                case pico2d.SDLK_d:
                    Player.P1.dir[0] += 1
                case pico2d.SDLK_r:
                    Player.P1.dir[2] = False
    elif MainScene.selectpos[0] == 1:
        if event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_RIGHT:             # 우측 이동
                    Player.P2.dir[0] += 1

                case pico2d.SDLK_LEFT:             # 좌측 이동
                    Player.P2.dir[0] -= 1
                case pico2d.SDLK_UP:
                    Player.P2.dir[2] = True
                case pico2d.SDLK_SPACE:
                    if Player.P2.motion == 'idle':
                        Player.P2.motion = 'dive'
                        Player.Move_Speed = Player.RUN_SPEED_PPS * 2
                        Player.player.bgm['motion'].play()
                        if Player.P2.dir[0] < 0:
                            Player.P2.dive_frame[0] = -1            # z키를 눌렀을때 어디 방향을 보고 있는지 입력
                        else:
                            Player.P2.dive_frame[0] = 1
                    elif Player.P2.motion == 'jump':
                        Player.P2.motion = 'spike'
                        Player.player.bgm['spike'].play()

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_RIGHT:
                    Player.P2.dir[0] -= 1
                case pico2d.SDLK_LEFT:
                    Player.P2.dir[0] += 1
                case pico2d.SDLK_UP:
                    Player.P2.dir[2] = False