from pico2d import *
import Player

def keyboard_input(event):
    if event.type == SDL_KEYDOWN:
        match event.key:
            case pico2d.SDLK_g:             # 우측 이동
                Player.P1.dir[0] += 1
            case pico2d.SDLK_d:             # 좌측 이동
                Player.P1.dir[0] -= 1
            case pico2d.SDLK_r:
                # if Player.P1.pos[1] == Player.floor:
                #     if Player.P1.motion != 'dive' and Player.P1.motion != 'Ldive':
                #         Player.P1.motion = 'jump'
                # Player.P1.dir[2] = True
                Player.P1.dir[2] = True
            case pico2d.SDLK_z:
                if Player.P1.motion == 'idle':
                    Player.P1.motion = 'dive'
                    Player.Move_Speed = Player.RUN_SPEED_PPS * 2
                    if Player.P1.dir[0] < 0:
                        Player.P1.dive_frame[0] = -1            # z키를 눌렀을때 어디 방향을 보고 있는지 입력
                    else:
                        Player.P1.dive_frame[0] = 1
                elif Player.P1.motion == 'jump':
                    Player.P1.motion = 'spike'

    elif event.type == SDL_KEYUP:
        match event.key:
            case pico2d.SDLK_g:
                Player.P1.dir[0] -= 1
            case pico2d.SDLK_d:
                Player.P1.dir[0] += 1
            case pico2d.SDLK_r:
                Player.P1.dir[2] = False

def main_input(event):
    pass