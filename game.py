from pbgetc import *
from levels import *

level1_objects = draw_level(level1)
player = Player(50, h - 90, 40, 50, 10, player_images)

level1_objects.add(player)

"КНОПКИ ДЛЯ МЕНЯ"
btn_play = Button(464, 250, 350, 100, (170, 139, 231), 'PLAY', 60, (255, 255, 255))
btn_exit = Button(465, 550, 350, 100, (170, 139, 231), 'EXIT', 60, (255, 255, 255))

mode = "menu"
game = True
finish = False
pygame.mixer.init()
pygame.mixer.music.load("BLOODBATH.ogg")

player = Player(50, h - 90, 40, 50, 10, player_images)

while game:
    key_pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if mode == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if btn_play.rect.collidepoint(x, y):
                    mode = "game"
                    pygame.mixer.music.play()
                if btn_exit.rect.collidepoint(x, y):
                    game = False
    
        
                        
    if mode == "menu":
        window.blit(bg, (0, 0))
        window.blit(game_name, (200, 50))

        btn_play.draw(120, 30)
        btn_exit.draw(120, 30)
    

    if mode == "game":
        if not finish:
            window.blit(bg, (0, 0))
            for obj in level1_objects:
                window.blit(obj.image, camera.apply(obj))
            camera.update(player)

            player.update(platforms)


            if player.rect.y > (h - player.rect.height):
                finish = True
    
    pygame.display.update()
    clock.tick(FPS)