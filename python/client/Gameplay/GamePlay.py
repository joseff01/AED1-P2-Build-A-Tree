import pygame, threading
from pygame.locals import *

from python.client.Gameplay.Node import Node
from python.client.Gameplay.Player import Player

frame = 0
count = 0


class gameplay:
    def __init__(self, screen, s, num):
        self.running = True
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
        self.currentChallenge = ""
        self.num = num
        self.socket = s
        self.screen = screen
        self.clock = pygame.time.Clock()
        receiveMessagesThread = threading.Thread(target=self.receiveMessage)
        receiveMessagesThread.start()
        self.playersList = []
        self.nodesList = []
        self.game()

    def game(self):

        player1 = Player(325, 415, 50, 50)
        player2 = Player(850, 415, 50, 50)
        self.playersList.extend((player1, player2))

        if self.num > 2:
            player3 = Player(496, 250, 50, 50)
            self.playersList.append(player3)
            if self.num > 3:
                player4 = Player(650, 257, 50, 50)
                self.playersList.append(player4)

        challengeRect = pygame.Rect(350, 630, 500, 30)

        while self.running:
            self.setBackground()

            pygame.draw.rect(self.screen, (255, 255, 255), challengeRect)

            player1.pressed = False
            player2.pressed = False
            if self.num > 2:
                player3.pressed = False
                if self.num > 3:
                    player4.pressed = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # checking for keypresses
                if event.type == pygame.KEYDOWN:
                    pNum = 0
                    for p in self.playersList:
                        keyL, keyR, keyUp = \
                            [(K_a, K_d, K_w), (K_f, K_h, K_t), (K_j, K_l, K_i), (K_LEFT, K_RIGHT, K_UP)][pNum]
                        if event.key == keyL:
                            p.left = True
                        if event.key == keyR:
                            p.right = True
                        if event.key == keyUp:
                            p.jump()
                        pNum += 1

                if event.type == pygame.KEYUP:
                    pNum = 0
                    for p in self.playersList:
                        keyL, keyR = \
                            [(K_a, K_d), (K_f, K_h), (K_j, K_l), (K_LEFT, K_RIGHT)][pNum]
                        if event.key == keyL:
                            p.left = False
                        if event.key == keyR:
                            p.right = False
                        pNum += 1

            # movimiento
            for p in self.playersList:
                p.move(self.playersList)

            if self.running:
                for player in self.playersList:
                    pygame.draw.rect(self.screen, (150, 0, 0), player.rect)

                pygame.display.flip()
                self.clock.tick(30)  # Aquí se controlan los FPS

    def checkColision(self, recPlayer1, recPlayer2, recPlayer3, recPlayer4, player1, player2, player3, player4):

        if recPlayer1.colliderect(recPlayer2) and (player1.pressed == True and player2.pressed == False):
            player1.colision(player2)
        elif recPlayer2.colliderect(recPlayer1) and (player2.pressed == True and player1.pressed == False):
            player2.colision(player1)

        if self.num == 3 or self.num == 4:
            if recPlayer3.colliderect(recPlayer1) and (player3.pressed == True and player1.pressed == False):
                player3.colision(player1)
            elif recPlayer3.colliderect(recPlayer2) and (player3.pressed == True and player2.pressed == False):
                player3.colision(player2)
            elif recPlayer1.colliderect(recPlayer3) and (player1.pressed == True and player3.pressed == False):
                player1.colision(player3)
            elif recPlayer2.colliderect(recPlayer3) and (player2.pressed == True and player3.pressed == False):
                player2.colision(player3)

            if self.num == 4:
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

    def setBackground(self):
        global frame, count
        if frame >= 19:
            frame = 0
        elif count == 2:
            frame += 1
            count = 0
        else:
            count += 1
        self.screen.blit(self.background_image[frame], [0, 0])

    def receiveMessage(self):
        import json
        while self.running:
            messageJSON = self.socket.recv(1024)
            # parse string
            stringJSON = str(messageJSON)[2:-5]
            if stringJSON[:6] == "server":
                continue
            # print(stringJSON)
            dicJSON = json.loads(stringJSON)
            print(dicJSON)
            if dicJSON['@type'][-5:] == "token":
                self.nodesList.append(Node((dicJSON['@type'], dicJSON['number'])))
