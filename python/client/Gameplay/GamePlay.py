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

        self.challengeTimer = None
        self.gameTimer = None
        self.currentChallenge = None
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
        gameTimerRect = pygame.Rect(425, 570, 50, 30)
        challengeTimerRect = pygame.Rect(540, 600, 30, 30)
        Font = pygame.font.SysFont("Century Gothic", 24)

        while self.running:
            self.setBackground()

            pygame.draw.rect(self.screen, (255, 255, 255), challengeRect)
            pygame.draw.rect(self.screen, (255, 255, 255), gameTimerRect)
            pygame.draw.rect(self.screen, (255, 255, 255), challengeTimerRect)
            if self.currentChallenge is not None:
                if self.currentChallenge["@type"] == "BMessage":
                    self.draw_text("Build a B Tree of order " + str(self.currentChallenge["order"])
                                   + " with " + str(self.currentChallenge["level"]) + " levels", Font,
                                   (0, 0, 0), self.screen, challengeRect.x, challengeRect.y)
                if self.currentChallenge["@type"] == "AVLMessage":
                    self.draw_text("Build an AVL Tree with " + str(self.currentChallenge["elementAmount"])
                                   + " elements", Font, (0, 0, 0), self.screen, challengeRect.x,
                                   challengeRect.y)
                if self.currentChallenge["@type"] == "BSTMessage":
                    self.draw_text("Build a BST Tree of depth " + str(self.currentChallenge["height"]),
                                   Font, (0, 0, 0), self.screen, challengeRect.x, challengeRect.y)
                if self.currentChallenge["@type"] == "SplayMessage":
                    self.draw_text("Build a Splay Tree with " + str(self.currentChallenge["elementAmount"])
                                   + " elements", Font, (0, 0, 0), self.screen, challengeRect.x, challengeRect.y)
            if self.challengeTimer is not None:
                self.draw_text(str(self.challengeTimer["timerNumber"]), Font, (0, 0, 0), self.screen, challengeTimerRect.x, challengeTimerRect.y)
            else:
                self.draw_text("60", Font, (0, 0, 0), self.screen, challengeTimerRect.x, challengeTimerRect.y)
            if self.gameTimer is not None:
                self.draw_text(str(self.gameTimer["timerNumber"]), Font, (0, 0, 0), self.screen, gameTimerRect.x, gameTimerRect.y)
            else:
                self.draw_text("600", Font, (0, 0, 0), self.screen, gameTimerRect.x, gameTimerRect.y)
            self.draw_text("Timer:", Font, (255, 255, 255), self.screen, gameTimerRect.x - 75, gameTimerRect.y)
            self.draw_text("Challenge Left:", Font, (255, 255, 255), self.screen, challengeTimerRect.x - 190, challengeTimerRect.y)
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
                continue
            if dicJSON['@type'] in {"BMessage", "AVLMessage", "BSTMessage", "SplayMessage"}:
                self.currentChallenge = dicJSON
                continue
            if dicJSON['@type'] == "TimerMessage":
                if dicJSON["timerType"] == "game":
                    self.gameTimer = dicJSON
                    continue
                if dicJSON["timerType"] == "challenge":
                    self.challengeTimer = dicJSON
                    continue



    def draw_text(self, text, font, color, surface, x, y):
        """
        Parameters: text, font, color, surface, x, y

        Return: None

        Restrictions1: text must be string, font must be pygame font object
        """
        if text == "":
            return
        text = font.render(text, 1, color)
        surface.blit(text, (x, y))
