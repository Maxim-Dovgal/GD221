import pygame

pygame.init()

w, h = 1200, 700
FPS = 60
coins_count = 0
level_count = 1

window = pygame.display.set_mode((w, h))
pygame.display.set_caption("GD")
pygame.display.set_icon(pygame.image.load("asstess/куб.png"))

clock = pygame.time.Clock()

#ГРУПИ СПРАЙТІВ#
platforms = pygame.sprite.Group()
spikes = pygame.sprite.Group()

#КАРТИНКИ СПРАЙТІВ#
bg = pygame.transform.scale((pygame.image.load("asstess/фон.png")),(w, h))

platform_image = pygame.image.load("asstess/блок.png")

player_images = [pygame.image.load("asstess/куб.png")]

spike_image = pygame.image.load("asstess/шип.png")
#ШРИФТИ#
pygame.font.init()
font1 = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 80)
font3 = pygame.font.SysFont(None, 160, bold=True)

#ТЕКСТИ#
game_name = font3.render("Geomeytry Dash", True, (116, 89, 170,), (155, 255, 255))
