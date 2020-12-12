import random

import pygame, threading
from pygame.locals import *

from python.client.Gameplay.Node import Node
from python.client.Gameplay.Player import Player
from python.client.Gameplay.Tree import Tree
from python.client.Gameplay.PowerUps import PowerUps

frame = 0
steps = 9
count = 0


class gameplay:
    def __init__(self, screen, s, num):
        self.running = True
        self.endGame = False
        # Todas las imagenes /////////////////////////////////////////////////////////////////////////////

        # background
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
        # movement
        self.greenSkinMove = [pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink0.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink1.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink2.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink3.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink4.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink5.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink6.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink7.png").convert_alpha(),
                              pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink8.png").convert_alpha()]
        self.greenSkinMoveR = [pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink0R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink1R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink2R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink3R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink4R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink5R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink6R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink7R.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink8R.png").convert_alpha()]
        self.greenSkinMoveF = [pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink0F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink1F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink2F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink3F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink4F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink5F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink6F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink7F.png").convert_alpha(),
                               pygame.image.load("Imgs\\Sprites\\GreenLink\\GLink8F.png").convert_alpha()]
        # shield
        self.shield = [pygame.image.load("Imgs\\Sprites\\Shield\\Shield0.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield1.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield2.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield3.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield4.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield5.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield6.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield7.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield8.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield9.png").convert_alpha(),
                       pygame.image.load("Imgs\\Sprites\\Shield\\Shield10.png").convert_alpha()]
        # weight
        self.pesa = [pygame.image.load("Imgs\\Sprites\\Weight\\Weight0.png").convert_alpha(),
                     pygame.image.load("Imgs\\Sprites\\Weight\\Weight1.png").convert_alpha(),
                     pygame.image.load("Imgs\\Sprites\\Weight\\Weight2.png").convert_alpha()]
        # wing
        self.wing = [pygame.image.load("Imgs\\Sprites\\Wing\\Wing0.png").convert_alpha(),
                     pygame.image.load("Imgs\\Sprites\\Wing\\Wing1.png").convert_alpha(),
                     pygame.image.load("Imgs\\Sprites\\Wing\\Wing2.png").convert_alpha(),
                     pygame.image.load("Imgs\\Sprites\\Wing\\Wing3.png").convert_alpha()]

        # ///////////////////////////////////////////////////////////////////////////////////////////////
        Node.Font = pygame.font.SysFont("Century Gothic", 20)  # Set font for nodes
        self.Font = pygame.font.SysFont("Century Gothic", 24)  # Set font of everything else
        self.link = pygame.image.load("Imgs\\Sprites\\GreenLink\\Link.png").convert_alpha()

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
        self.playerPointList = [0, 0]
        self.nodesList = []
        self.powerUpsList = []
        self.game()

    def game(self):

        player1 = Player(325, 415, 50, 50, 1)
        self.screen.blit(self.link, (player1.rect.x, player1.rect.y))
        player2 = Player(850, 415, 50, 50, 1)
        self.playersList.extend((player1, player2))

        if self.num > 2:
            player3 = Player(496, 250, 50, 50, 1)
            self.playersList.append(player3)
            self.playerPointList.append(0)
            if self.num > 3:
                player4 = Player(650, 257, 50, 50, 1)
                self.playersList.append(player4)
                self.playerPointList.append(0)

        challengeRect = pygame.Rect(350, 630, 500, 30)
        gameTimerRect = pygame.Rect(425, 570, 50, 30)
        challengeTimerRect = pygame.Rect(540, 600, 30, 30)
        player1PointRect = pygame.Rect(400, 530, 80, 30)
        player2PointRect = pygame.Rect(500, 530, 80, 30)
        player3PointRect = pygame.Rect(600, 530, 80, 30)
        player4PointRect = pygame.Rect(700, 530, 80, 30)

        winnerSurface = pygame.Surface((1000, 474))
        winnerSurface.set_alpha(128)
        winnerSurface.fill((255, 255, 255))

        pointRecs = [player1PointRect, player2PointRect, player3PointRect, player4PointRect]

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if self.endGame:
                        self.running = False
                    else:
                        self.socket.send("Stop Server Connection\n".encode())
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
                            p.setMoveCount(0)

                        if event.key == keyR:
                            p.right = False
                            p.setMoveCount(0)
                        pNum += 1

            # movimiento
            for p in self.playersList:
                p.move(self.playersList)

            # manejo de nodos
            for n in self.nodesList:
                if not self.endGame:
                    n.fall(self.nodesList)
                    if n.check_catch(self.playersList):
                        n.delete(self.nodesList)
                        n.send(self.socket)

            for power in self.powerUpsList:
                if not self.endGame:
                    power.fall(self.powerUpsList)
                    if power.catchCheck(self.playersList):
                        power.deletePow(self.powerUpsList)

            rNum = random.randint(1, 400)

            if ((rNum == 1 or rNum == 2) or rNum == 3) and not self.endGame:
                self.powerUpsList.append(PowerUps(rNum))

            if self.running:
                # pintar fondo
                self.setBackground()
                # pintar sidebar
                self.setTreeSidebar()
                # pintar jugadores
                for player in self.playersList:
                    # pintar árboles de los jugadores
                    if player.tree is not None:
                        player.tree.draw(self.screen)
                    if player.moveCount == 8:
                        player.setMoveCount(0)
                    else:
                        player.setMoveCount(player.moveCount + 1)
                    '''
                    if player.falling:
                        if player.fallingCount == 8:
                            player.setfallingCount(0)
                        else:
                            player.setfallingCount(player.fallingCount + 1)
                        self.screen.blit(self.greenSkinMoveF[player.fallingCount], (player.rect.x, player.rect.y))
                    '''
                    if player.left:
                        self.screen.blit(self.greenSkinMove[player.moveCount], (player.rect.x, player.rect.y))
                    elif player.right:
                        self.screen.blit(self.greenSkinMoveR[player.moveCount], (player.rect.x, player.rect.y))

                    else:
                        self.screen.blit(self.link, (player.rect.x, player.rect.y))

                for n in self.nodesList:
                    n.draw(self.screen)

                for pow in self.powerUpsList:
                    if pow.type == 1:
                        if pow.count == 3:
                            pow.setCount(0)
                        else:
                            pow.setCount(pow.count + 1)
                        self.screen.blit(self.wing[pow.count], (pow.rect.x, pow.rect.y))
                    if pow.type == 2:
                        if pow.count == 10:
                            pow.setCount(0)
                        else:
                            pow.setCount(pow.count + 1)
                        self.screen.blit(self.shield[pow.count], (pow.rect.x, pow.rect.y))
                    if pow.type == 3:
                        if pow.count == 1:
                            pow.setCount(0)
                        else:
                            pow.setCount(pow.count + 1)
                        self.screen.blit(self.pesa[pow.count], (pow.rect.x, pow.rect.y))

                # pintar rects para info de challenges y timer
                pygame.draw.rect(self.screen, (255, 255, 255), challengeRect)
                pygame.draw.rect(self.screen, (255, 255, 255), gameTimerRect)
                pygame.draw.rect(self.screen, (255, 255, 255), challengeTimerRect)
                pygame.draw.rect(self.screen, (255, 255, 255), player1PointRect)
                pygame.draw.rect(self.screen, (255, 255, 255), player2PointRect)
                pygame.draw.rect(self.screen, (255, 255, 255), player3PointRect)
                pygame.draw.rect(self.screen, (255, 255, 255), player4PointRect)
                # info de challenges y timer
                self.setChallenge(challengeRect, challengeTimerRect)
                self.setPlayerPoints(pointRecs)
                self.setTimer(gameTimerRect)
                self.draw_text("Timer:", self.Font, (255, 255, 255), self.screen, gameTimerRect.x - 75, gameTimerRect.y)
                self.draw_text("Challenge Left:", self.Font, (255, 255, 255), self.screen, challengeTimerRect.x - 190,
                               challengeTimerRect.y)
                if self.endGame:
                    endGameFont0 = pygame.font.SysFont("Century Gothic", 30)
                    self.screen.blit(winnerSurface, (100, 100))
                    self.draw_text("GAME OVER", endGameFont0, (0, 0, 0), self.screen, 486, 115)
                    self.draw_text("Total Points", endGameFont0, (0, 0, 0), self.screen, 486, 150)
                    self.draw_text("Player 1:       " + str(self.playerPointList[0]), self.Font, (0, 0, 0), self.screen,
                                   450, 200)
                    self.draw_text("Player 2:       " + str(self.playerPointList[1]), self.Font, (0, 0, 0), self.screen,
                                   450, 250)
                    if self.num > 2:
                        self.draw_text("Player 3:       " + str(self.playerPointList[2]), self.Font, (0, 0, 0),
                                       self.screen, 450, 300)
                        if self.num > 3:
                            self.draw_text("Player 4:       " + str(self.playerPointList[3]), self.Font, (0, 0, 0),
                                           self.screen, 450, 350)
                    winner = []
                    for i in range(self.num):
                        if not winner or winner[0][0] == self.playerPointList[i]:
                            winner.append((self.playerPointList[i], i + 1))
                        if winner[0][0] < self.playerPointList[i]:
                            winner = [self.playerPointList[i], i + 1]
                    if len(winner) > 1:
                        self.draw_text("Winners:", endGameFont0, (0, 0, 0), self.screen, 200, 500)
                        x = 350
                        for i in range(len(winner)):
                            self.draw_text("Player " + str(winner[i][1]), endGameFont0, (0, 0, 0), self.screen, x, 500)
                            x += 150
                    else:
                        self.draw_text("Winner: Player " + str(winner[0][1]), endGameFont0, (0, 0, 0), self.screen, 450,
                                       500)

                pygame.display.flip()
                self.clock.tick(30)  # Aquí se controlan los FPS

    def setTreeSidebar(self):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        LIGHTYELLOW = (242, 212, 143)
        pygame.draw.rect(self.screen, LIGHTYELLOW, (1200, 0, 300, 674))
        pygame.draw.rect(self.screen, BLACK, (1200, 0, 300, 674), 4)
        for n in range(4):  # 1-3
            pygame.draw.line(self.screen, BLACK, (1200, n * 674 / 4), (1500, n * 674 / 4), 4)
        for n in range(self.num):
            self.draw_text("Jugador " + str(n + 1), self.Font, BLACK, self.screen, 1210, 2 + n * 674 / 4)

    def setChallenge(self, challengeRect, challengeTimerRect):
        Font = self.Font
        BLACK = (0, 0, 0)
        BLUE = (32, 28, 176)
        RED = (171, 10, 10)
        GREEN = (1, 135, 6)
        YELLOW = (235, 192, 52)

        if self.currentChallenge is not None:
            if self.currentChallenge["@type"] == "BMessage":
                self.draw_text("Build a B Tree of order " + str(self.currentChallenge["order"])
                               + " with " + str(self.currentChallenge["level"]) + " levels", Font,
                               RED, self.screen, challengeRect.x, challengeRect.y)
                for player in self.playersList:
                    if player.tree is not None:
                        player.tree.set_BTree_order(self.currentChallenge['order'])
            if self.currentChallenge["@type"] == "AVLMessage":
                self.draw_text("Build an AVL Tree with " + str(self.currentChallenge["elementAmount"])
                               + " elements", Font, BLUE, self.screen, challengeRect.x,
                               challengeRect.y)
            if self.currentChallenge["@type"] == "BSTMessage":
                self.draw_text("Build a BST Tree of depth " + str(self.currentChallenge["height"]),
                               Font, YELLOW, self.screen, challengeRect.x, challengeRect.y)
            if self.currentChallenge["@type"] == "SplayMessage":
                self.draw_text("Build a Splay Tree with " + str(self.currentChallenge["elementAmount"])
                               + " elements", Font, GREEN, self.screen, challengeRect.x, challengeRect.y)
            if self.challengeTimer is not None:
                self.draw_text(str(self.challengeTimer["timerNumber"]), Font, BLACK, self.screen,
                               challengeTimerRect.x, challengeTimerRect.y)
            else:
                self.draw_text("60", Font, BLACK, self.screen, challengeTimerRect.x, challengeTimerRect.y)

    def setPlayerPoints(self, recs):
        Font = self.Font
        BLACK = (0, 0, 0)
        WHITE = (255, 255, 255)
        for i in range(self.num):
            self.draw_text(str(self.playerPointList[i]), Font, BLACK, self.screen, recs[i].x, recs[i].y)
            self.draw_text("Player " + str(i + 1), Font, WHITE, self.screen, recs[i].x, recs[i].y - 30)

    def setTimer(self, gameTimerRect):
        Font = self.Font
        if self.gameTimer is not None:
            self.draw_text(str(self.gameTimer["timerNumber"]), Font, (0, 0, 0), self.screen, gameTimerRect.x,
                           gameTimerRect.y)
        else:
            self.draw_text("610", Font, (0, 0, 0), self.screen, gameTimerRect.x, gameTimerRect.y)

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
        while self.running and not self.endGame:
            messageJSON = self.socket.recv(1024)
            # parse string
            # print(messageJSON)
            stringJSON = str(messageJSON)[2:-5]
            # print(stringJSON)
            if stringJSON[:6] == "server":
                continue
            dicJSON = json.loads(stringJSON)
            print(dicJSON)
            if dicJSON['@type'][-5:] == "Token":
                self.nodesList.append(Node(dicJSON['@type'], dicJSON['number']))
                continue
            elif dicJSON['@type'][-7:] == "Message":
                if dicJSON['@type'] == "TimerMessage":
                    if dicJSON["timerType"] == "game":
                        self.gameTimer = dicJSON
                        continue
                    if dicJSON["timerType"] == "challenge":
                        self.challengeTimer = dicJSON
                        continue
                if dicJSON['@type'] == "EndGameMessage":
                    self.endGame = True
                    self.socket.send("Stop Server Connection\n".encode())
                    continue
                else:
                    self.currentChallenge = dicJSON
                    continue
            elif dicJSON['@type'][-4:] == "Tree":
                self.playersList[dicJSON['owner'] - 1].tree = Tree(dicJSON)
                continue

            elif dicJSON['@type'][-6:] == "Points":
                self.playerPointList[dicJSON["player"]] += 100
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
