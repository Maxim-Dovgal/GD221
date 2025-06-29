from pbgetc import *
from settings import *

level1 = [
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                               ----------^---^---^^^-----------------^^"
    "  ---------^^^--------^^^-----^                                        "

]
level1_width = len(level1[0]) * 50
level1_height = len(level1) * 50

level2 = [
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                                                                       "
    "                               ----------^---^---^^^-----------------^^"
    "------------^^^--------^^^-----^                                       "

]
level2_width = len(level2[0]) * 50
level2_height = len(level2) * 50

level_objects = pygame.sprite.Group()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)
    
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)
    
def camera_config(camera, target_ract):
    l, t, _, _ = target_ract
    _, _, w, h = camera
    l, t = -l + w / 2, -t + h / 2

    l = min(0, 1)
    l = max(-(camera.width - w), l)
    t = max(-(camera.height - h), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

camera = Camera(camera_config, level1_width, level1_height)

def draw_level(level: list):
    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 30, platform_image)
                level_objects.add(platform)
                platforms.add(platform)
            if symbol == "^":
                spike = MapObject(x, y, 30, 30, spike_image)
                level_objects.add(spike)
                spikes.add(spike)

            x += 100
        x = 0
        y += 30

    return level_objects








