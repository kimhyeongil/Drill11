# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, load_font, clamp, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from ball import Ball, BigBall
import game_world
import game_framework

PIXEL_PER_METER = 100 / 3
RUN_SPEED_PPS = 20 * PIXEL_PER_METER

FRAMES_PER_TIME = 14  # 액션 프레임 증가 속도

BIRD_METER_SIZE = 3
BIRD_PIXEL_SIZE = BIRD_METER_SIZE * PIXEL_PER_METER
class Bird:
    def __init__(self):
        self.x, self.y = 800, 400
        self.frame = 0
        self.face_dir = 1
        self.dir = 1
        self.l = [34, 216, 398, 555, 728, 34, 216, 398, 580, 762, 34, 216, 376,546]
        self.t = [1, 2, 12, 17, 48, 217, 216, 216, 217, 219, 392, 394, 395,370]
        self.w = [146, 146, 146, 171, 182, 146, 146, 146, 146, 146, 146, 146, 168,180]
        self.h = [143, 141, 130, 122, 88, 118, 124, 120, 109, 110, 108, 106, 88,114]
        self.image = load_image('bird_animation.png')
        for i in range(len(self.t)):
            self.t[i] += self.h[i]
        print(self.t)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_TIME * game_framework.frame_time) % len(self.l)
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x >= 1600:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def handle_event(self, event):
        pass

    def draw(self):
        frame = int(self.frame)
        print(frame)
        if self.dir == -1:
            self.image.clip_composite_draw(self.l[frame], self.image.h - self.t[frame], self.w[frame], 143, 0,'h',self.x, self.y, BIRD_PIXEL_SIZE, BIRD_PIXEL_SIZE)
        else:
            self.image.clip_draw(self.l[frame], self.image.h - self.t[frame], self.w[frame], 143, self.x, self.y, BIRD_PIXEL_SIZE, BIRD_PIXEL_SIZE)
