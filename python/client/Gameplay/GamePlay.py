import pygame, threading

from python.client.Gameplay.Player import player
from pygame.locals import *

frame = 0


class gameplay:
    def __init__(self, screen, s, num):
        self.running = False
        self.background_image = [pygame.image.load("Imgs\\GamePlay\\bgGame0.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame1.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame2.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame3.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame4.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame5.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame6.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame7.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame8.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame9.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame10.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame11.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame12.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame13.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame14.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame15.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame16.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame17.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame18.png").convert(),
                            pygame.image.load("Imgs\\GamePlay\\bgGame19.png").convert()]
        self.num = num
        self.socket = s
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game()

        receiveMessagesThread = threading.Thread(target=self.receiveMessage)
        receiveMessagesThread.start()

    def game(self):
        playersList=[]

        player1 = player(325, 415, 50, 50)
        player2 = player(850, 415, 50, 50)
        playersList.extend((player1,player2))
        if self.num > 2:
            player3 = player(496, 250, 50, 50)
            playersList.append(player3)
            if self.num > 3:
                player4 = player(650, 257, 50, 50)
                playersList.append(player4)

        while self.running:
            self.setBackground()
            keys = pygame.key.get_pressed()
            self.checkPressed()

            player1.pressed = False
            player2.pressed = False
            if self.num > 2:
                player3.pressed = False
                if self.num > 3:
                    player4.pressed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                #checking for keypresses
                if event.type == pygame.KEYDOWN:
                    pNum = 1
                    for p in playersList:
                        keyL,keyR,keyUp = [(K_a,K_d,K_w),(K_f,K_h,K_t),(K_j,K_l,K_i),(K_LEFT,K_RIGHT,K_UP)][pNum]
                        if event.key == keyL:
                            p.left = True
                        if event.key == keyR:
                            p.right=True
                        if event.key == keyUp:
                            p.jump()
                        pNum+=1

                if event.type == pygame.KEYUP:
                    pNum = 1
                    for p in playersList:
                        keyL, keyR, keyUp = \
                        [(K_a, K_d), (K_f, K_h), (K_j, K_l), (K_LEFT, K_RIGHT)][pNum]
                        if event.key == keyL:
                            p.left = False
                        if event.key == keyR:
                            p.right = False
                        pNum += 1

            #hitboxes
            recPlayer1 = pygame.Rect(player1.x, player1.y, 50, 50)
            recPlayer2 = pygame.Rect(player2.x, player2.y, 50, 50)

            if self.num > 2:
                recPlayer3 = pygame.Rect(player3.x, player3.y, 50, 50)
                if self.num > 3:
                    recPlayer4 = pygame.Rect(player4.x, player4.y, 50, 50)

            #movimiento
            for p in playersList:
                p.move(left, right)

            if self.running:
                self.spawnBichito()
                self.checkColision()

                pygame.display.flip()
                self.clock.tick(30)

    def movePlayers(self, playersList):

    def checkColision(self, recPlayer1,recPlayer2,recPlayer3,recPlayer4):

        if recPlayer1.colliderect(recPlayer2) and (player1.pressed == True and player2.pressed == False):
            player1.colision(player2)
        elif recPlayer2.colliderect(recPlayer1) and (player2.pressed == True and player1.pressed == False):
            player2.colision(player1)

        if num == 3 or num == 4:
            if recPlayer3.colliderect(recPlayer1) and (player3.pressed == True and player1.pressed == False):
                player3.colision(player1)
            elif recPlayer3.colliderect(recPlayer2) and (player3.pressed == True and player2.pressed == False):
                player3.colision(player2)
            elif recPlayer1.colliderect(recPlayer3) and (player1.pressed == True and player3.pressed == False):
                player1.colision(player3)
            elif recPlayer2.colliderect(recPlayer3) and (player2.pressed == True and player3.pressed == False):
                player2.colision(player3)

            if num == 4:
                if recPlayer4.colliderect(recPlayer1) and (player4.pressed == True and player1.pressed == False):
                    player4.colision(player1)
                elif recPlayer4.colliderect(recPlayer2) and (player4.pressed == True and player2.pressed == False):
                    player4.colision(player2)
                elif recPlayer4.colliderect(recPlayer3) and (player4.pressed == True and player3.pressed == False):
                    player4.colision(player3)
                elif recPlayer1.colliderect(recPlayer4) and (player1.pressed == True and player4.pressed == False):
                    player1.colision(player4)
                elif recPlayer2.colliderect(recPlayer4) and (player2.pressed == True and player4.pressed == False):
                    player2.colision(player4)
                elif recPlayer3.colliderect(recPlayer4) and (player3.pressed == True and player4.pressed == False):
                    player3.colision(player4)



    def spawnBichito(self):
        leftCroc = pygame.Rect(300, 373, 105, 20)

        pygame.draw.rect(self.screen, (100, 0, 0), leftCroc)
        pygame.draw.rect(self.screen, (100, 0, 0), recPlayer1)
        pygame.draw.rect(self.screen, (100, 0, 0), recPlayer2)
        if self.num == 3:
            pygame.draw.rect(self.screen, (100, 0, 0), [player3.x, player3.y, 50, 50])
        elif self.num == 4:
            pygame.draw.rect(self.screen, (100, 0, 0), [player3.x, player3.y, 50, 50])
            pygame.draw.rect(self.screen, (100, 0, 0), [player4.x, player4.y, 50, 50])

    def setBackground(self):
        global frame
        self.screen.blit(self.background_image[frame], [0, 0])
        frame += 1
        if frame >= 19:
            frame = 0

    def receiveMessage(self):
        while self.running:
            messageJSON = self.socket.recv(1024)
            print(messageJSON)