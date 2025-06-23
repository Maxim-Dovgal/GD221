from settings import *

class MapObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed,  images):
        super().__init__()
        self.width = width
        self.height = height
        self.images = images
        self.anim_count = 0
        self.image = pygame.transform.scale(self.images[self.anim_count], (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Sprite):
    def __init__(self, x, y, width, height, speed, images):
        super().__init__(x, y, width, height, speed, images)

        self.is_jump = False
        self.jump_count = 25

        self.fall = 0
        self.gravity = 2,5
        self.on_ground = False

    def update(self, platforms):
        self.image = pygame.transform.scale(pygame.image.load("куб.png"), (self.width, self.height))


        self.fall += self.gravity
        self.rect.y += self.fall
        hit_platforms = pygame.sprite.spritecollide(self, platforms, False)
        if hit_platforms:
            for platform in hit_platforms:
                if self.fall > 0 and self.rect.bottom > platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.fall = 0
                    self.on_ground = True
        else:
            self.on_ground = False

        keys_pressed = pygame.key.get_pressed()

        if not self.is_jump:
            if keys_pressed[pygame.K_SPACE]:
                if self.on_ground:
                    self.is_jump = True
                    self.fall -= self.jump_count
        else:
            self.is_jump = not self.on_ground


class Button:
    def __init__(self, x, y, w, h, color, text, txt_size, txt_color):
        self.w = w
        self.h = h
        self.color = color

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.text = pygame.font.Font(None, txt_size).render(text, True, txt_color)
        
    def draw(self, shift_x, shift_y):
        window.blit(self.image, (self.rect.x, self.rect.y))
        window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))
        
        
        