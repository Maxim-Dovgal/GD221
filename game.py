from pbgetc import *
from levels import *

level1_objects = draw_level(level1)
player = Player(50, h - 90, 40, 50, 8, player_images)

level1_objects.add(player)

"КНОПКИ ДЛЯ МЕНЯ"
btn_play = Button(464, 250, 350, 100, (170, 139, 231), 'PLAY', 60, (255, 255, 255))
btn_exit = Button(465, 550, 350, 100, (170, 139, 231), 'EXIT', 60, (255, 255, 255))

mode = "menu"
game = True
finish = False
pygame.mixer.init()
lose_sound = pygame.mixer.Sound("lose.mp3")
pygame.mixer.music.load("BLOODBATH.ogg")


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

            if pygame.sprite.spritecollide(player, spikes, False):
                finish = True
                pygame.mixer.music.pause()
                lose_sound.play()
                window.blit(game_lose, (600, 300))

            

            if player.rect.y > (h - player.rect.height):
                finish = True
                pygame.mixer.music.pause()
    
    pygame.display.update()
    clock.tick(FPS)