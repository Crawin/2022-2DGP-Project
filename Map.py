from pico2d import *
import Sprite
# 2, 263 , 434,199
# 맵 크기 = 448 x 448
# 맵 타일 크기 16 x 16
# 산 크기

def draw():
    clear_canvas()
    for y in range(16, 432 + 1, 32):
        for x in range(16, 432 + 1, 32):
            Sprite.sprite_sheets[0].clip_draw(138, 885 - 18, 16, 16, x, y, 32, 32)      # 해안가

    Sprite.sprite_sheets[0].clip_draw(84, 885 - 18, 16, 16, 16, 16 + 32 * 2, 32, 32)  # 바닥 선 /
    for i in range(1, 13):
        Sprite.sprite_sheets[0].clip_draw(66, 885 - 18, 16, 16, 16 + 32 * i, 16 + 32 * 2, 32, 32)  # 바닥 선 =
    Sprite.sprite_sheets[0].clip_draw(102, 885 - 18, 16, 16, 432, 16 + 32 * 2, 32, 32)  # 바닥 선 \

    for x in range(16, 432 + 1, 32):
        Sprite.sprite_sheets[0].clip_draw(120, 885 - 18, 16, 16, x, 16 + 32 * 3, 32, 32)  # 빨간선

    Sprite.sprite_sheets[0].clip_draw(2, 885 - 264, 434 - 2, 263 - 199, 448 / 2, 32 * 5, 449, 64)       # 산

    for y in range(208, 432 + 1, 32):
        for x in range(16, 432 + 1, 32):
            Sprite.sprite_sheets[0].clip_draw(156, 885 - 18, 16, 16, x, y, 32, 32)      # 하늘