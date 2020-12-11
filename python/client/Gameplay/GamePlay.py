import pygame, threading
from pygame.locals import *

from python.client.Gameplay.Node import Node
from python.client.Gameplay.Player import Player

frame = 0
steps = 9
count = 0


class gameplay:
    def __init__(self, screen, s, num):
        self.running = True
        #Todas las imagenes /////////////////////////////////////////////////////////////////////////////

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

        #///////////////////////////////////////////////////////////////////////////////////////////////
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
        self.nodesList = []
        self.game()

    def game(self):

        player1 = Player(325, 415, 50, 50,1)
        self.screen.blit(self.link,(player1.rect.x,player1.rect.y))
        player2 = Player(850, 415, 50, 50,1)
        self.playersList.extend((player1, player2))

        if self.num > 2:
            player3 = Player(496, 250, 50, 50,1)
            self.playersList.append(player3)
            if self.num > 3:
                player4 = Player(650, 257, 50, 50,1)
                self.playersList.append(player4)

        challengeRect = pygame.Rect(350, 630, 500, 30)
        gameTimerRect = pygame.Rect(425, 570, 50, 30)
        challengeTimerRect = pygame.Rect(540, 600, 30, 30)

        while self.running:

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
                n.fall(self.nodesList)
                if n.check_catch(self.playersList):
                    n.delete(self.nodesList)
                    n.send(self.socket)

            if self.running:
                # pintar fondo
                self.setBackground()
                # pintar sidebar
                self.setTreeSidebar()
                # pintar jugadores
                for player in self.playersList:
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
                # pintar rects para info de challenges y timer
                pygame.draw.rect(self.screen, (255, 255, 255), challengeRect)
                pygame.draw.rect(self.screen, (255, 255, 255), gameTimerRect)
                pygame.draw.rect(self.screen, (255, 255, 255), challengeTimerRect)
                # info de challenges y timer
                self.setChallenge(challengeRect, challengeTimerRect)
                self.setTimer(gameTimerRect)
                self.draw_text("Timer:", self.Font, (255, 255, 255), self.screen, gameTimerRect.x - 75, gameTimerRect.y)
                self.draw_text("Challenge Left:", self.Font, (255, 255, 255), self.screen, challengeTimerRect.x - 190,
                               challengeTimerRect.y)

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
                               YELLOW, self.screen, challengeRect.x, challengeRect.y)
            if self.currentChallenge["@type"] == "AVLMessage":
                self.draw_text("Build an AVL Tree with " + str(self.currentChallenge["elementAmount"])
                               + " elements", Font, BLUE, self.screen, challengeRect.x,
                               challengeRect.y)
            if self.currentChallenge["@type"] == "BSTMessage":
                self.draw_text("Build a BST Tree of depth " + str(self.currentChallenge["height"]),
                               Font, RED, self.screen, challengeRect.x, challengeRect.y)
            if self.currentChallenge["@type"] == "SplayMessage":
                self.draw_text("Build a Splay Tree with " + str(self.currentChallenge["elementAmount"])
                               + " elements", Font, GREEN, self.screen, challengeRect.x, challengeRect.y)
            if self.challengeTimer is not None:
                self.draw_text(str(self.challengeTimer["timerNumber"]), Font, BLACK, self.screen,
                               challengeTimerRect.x, challengeTimerRect.y)
            else:
                self.draw_text("60", Font, BLACK, self.screen, challengeTimerRect.x, challengeTimerRect.y)

    def setTimer(self, gameTimerRect):
        Font = self.Font
        if self.gameTimer is not None:
            self.draw_text(str(self.gameTimer["timerNumber"]), Font, (0, 0, 0), self.screen, gameTimerRect.x,
                           gameTimerRect.y)
        else:
            self.draw_text("600", Font, (0, 0, 0), self.screen, gameTimerRect.x, gameTimerRect.y)

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
            if dicJSON['@type'][-5:] == "Token":
                self.nodesList.append(Node(dicJSON['@type'], dicJSON['number']))
                continue
            if dicJSON['@type'][-7:] == "Message":
                if dicJSON['@type'] == "TimerMessage":
                    if dicJSON["timerType"] == "game":
                        self.gameTimer = dicJSON
                        continue
                    if dicJSON["timerType"] == "challenge":
                        self.challengeTimer = dicJSON
                        continue
                self.currentChallenge = dicJSON
                continue
            if dicJSON['@type'] [-4:] == "Tree":
                # Recibir Arboles
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
