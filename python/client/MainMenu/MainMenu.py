from time import sleep
from python.client.GameplayMenu.GamePlayMenu import gameplay
import pygame

pygame.init()

class MainMenu:
    def __init__(self):

        run = False
        frame = 0

        screen = pygame.display.set_mode((1200, 674))
        pygame.display.set_caption("Smash Bros")

        background_image = [pygame.image.load("Imgs\\Bg1.png"), pygame.image.load("Imgs\\Bg2.png"),
                            pygame.image.load("Imgs\\Bg3.png"), pygame.image.load("Imgs\\Bg4.png"),
                            pygame.image.load("Imgs\\Bg5.png"), pygame.image.load("Imgs\\Bg6.png"),
                            pygame.image.load("Imgs\\Bg7.png"), pygame.image.load("Imgs\\Bg8.png")]

        rec = pygame.Rect(540, 306, 170, 100)
        click = False

        while (run == False):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sleep(0.1)
                    click = True
                if event.type == pygame.MOUSEBUTTONUP:
                    click = False

            screen.blit(background_image[frame], [0, 0])
            screen.blit(pygame.image.load("Imgs\\Logo.png"), [290, -20])
            frame += 1

            if frame >= 8:
                frame = 0

            if rec.collidepoint(pygame.mouse.get_pos()) and click == True:
                screen.blit(pygame.image.load("Imgs\\playButtonOn.png"), [510, 300])
                run = True
                print("hewo")
                gameplay(screen)

            elif rec.collidepoint(pygame.mouse.get_pos()):
                screen.blit(pygame.image.load("Imgs\\playButtonOn.png"), [510, 305])
            else:
                screen.blit(pygame.image.load("Imgs\\playButton.png"), [510, 305])

            sleep(0.1)
            pygame.display.update()

play = MainMenu()