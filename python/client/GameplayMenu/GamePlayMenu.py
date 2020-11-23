from time import sleep
import pygame


frame = 0


class gameplay:
    def __init__(self, screen):
        dead = False

        background_image = [pygame.image.load("Imgs\\GamePlay\\bgGame0.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame1.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame2.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame3.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame4.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame5.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame6.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame7.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame8.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame9.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame10.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame11.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame12.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame13.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame14.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame15.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame16.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame17.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame18.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame19.png")]

        # COLISIONES

        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 375, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 20)
        rightStand = pygame.Rect(639, 300, 76, 20)
        rightBirb = pygame.Rect(795, 373, 105, 20)

        xcord = 600
        ycord = 415

        def spawnBichito():
            pygame.draw.rect(screen, (100, 0, 0), [xcord, ycord, 50, 50])
            pygame.display.update()

        def setBackground():
            global frame
            screen.blit(background_image[frame], [0, 0])
            frame += 1
            sleep(0.1)
            if frame >= 19:
                frame = 0

        while (dead == False):
            setBackground()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True
                elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    if event.key == ord('d'):
                        xcord += 10
                    if event.key == ord('a'):
                        xcord -= 10

            spawnBichito()

