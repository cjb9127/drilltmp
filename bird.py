import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y, self.fly_speed = random.randint(0, 1600-1), random.randint(300+50, 600-50), random.randint(-40, 40)
        self.frame = random.randint(0, 13)
        self.velocity = 100

    def draw(self):
         Bird.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        # self.frame = (self.frame + 1) % 14
        # self.x -= self.fly_speed * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(50, self.x, 1600 - 50)
        if self.x == 50 or self.x == 1550:
            self.velocity *= -1


