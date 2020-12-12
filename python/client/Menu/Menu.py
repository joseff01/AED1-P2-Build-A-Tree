from python.client.Gameplay.GamePlay import gameplay
import pygame, socket, sys
from pygame.locals import *

pygame.init()


class Menu:
    def __init__(self):
        """
        Crea el menu principal del videojuego, permite que el usuario escoja cuantos jugadores van a jugar y conecta el servidor con el cliente
        Authors: Mariana, Ignacio
        Creates the main window, the main clock and calls main_menu().
        """
        self.screen = pygame.display.set_mode((1500, 674))
        self.clock = pygame.time.Clock()

        self.main_menu()

    def connect_menu(self, playerNum):
        """
        Conecta el menu con el servidor y activa GamePlay
        Authors: Ignacio, Jose Antonio
        :param playerNum:
        :return:
        Restrictions: playerNum must be an int
        """
        running = True

        backgroundImg = pygame.image.load("Imgs\\beforeImage2.png").convert()
        copperplateFont = pygame.font.SysFont("copperplate gothic", 32)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        ipBox = pygame.Rect(400, 200, 550, 50)
        portBox = pygame.Rect(400, 300, 550, 50)

        self.screen.blit(backgroundImg, [0, 0])
        self.draw_text("Server IP:", copperplateFont, BLACK, self.screen, ipBox.x - 190, ipBox.y + 10)
        self.draw_text("Server Port:", copperplateFont, BLACK, self.screen, portBox.x - 290, portBox.y + 10)

        ipActive = False
        portActive = False
        ipString = ""
        portString = ""

        while running:

            click = False
            for event in pygame.event.get():  # check events here
                if event.type == QUIT:  # leave application
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if ipActive:
                        if event.key == pygame.K_BACKSPACE:
                            ipString = ipString[:-1]
                        elif len(ipString) < 18:
                            ipString += event.unicode
                    elif portActive:
                        if event.key == pygame.K_BACKSPACE:
                            portString = portString[:-1]
                        elif len(portString) < 5:
                            portString += event.unicode

                    if event.key == pygame.K_RETURN:
                        if (ipString == "127.0.0.1" or ipString.upper() == "LOCALHOST"):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.connect(("127.0.0.1", int(portString)))
                                s.send("Start Server Connection\n".encode())
                                gameplay(self.screen, s, playerNum)
                                running = False
                            except socket.error:
                                print("Could not connect to Server, try another socket or IP")
                        else:
                            print("Could not connect to Server, try another socket or IP")
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse click
                    click = True

            mx, my = pygame.mouse.get_pos()
            if ipBox.collidepoint((mx, my)) and click:
                ipActive = True
                portActive = False
            elif portBox.collidepoint((mx, my)) and click:
                ipActive = False
                portActive = True

            if running:  # tal vez ocupe agregar un blit al fondo
                pygame.draw.rect(self.screen, WHITE, ipBox)
                pygame.draw.rect(self.screen, WHITE, portBox)
                self.draw_text(ipString, copperplateFont, BLACK, self.screen, ipBox.x + 5, ipBox.y + 5)
                self.draw_text(portString, copperplateFont, BLACK, self.screen, portBox.x + 5, portBox.y + 5)

                pygame.display.flip()
                self.clock.tick(60)

    def choose_menu(self):
        """
        Muestra un menu que le permite al jugador escoger la cantidad de jugadores
        Authors:Mariana, Ignacio
        :return:
        """
        running = True

        backgroundImg = pygame.image.load("Imgs\\beforeImage.png").convert()
        self.screen.blit(backgroundImg, [0, 0])

        # elemento 0 = apagado, 1 = encendido (Escogido)
        twoButtonImg = [pygame.image.load("Imgs\\twoPlayers.png").convert_alpha(),
                        pygame.image.load("Imgs\\twoPlayersChoose.png").convert_alpha()]
        threeButtonImg = [pygame.image.load("Imgs\\threePlayers.png").convert_alpha(),
                          pygame.image.load("Imgs\\threePlayersChoose.png").convert_alpha()]
        fourButtonImg = [pygame.image.load("Imgs\\fourPlayers.png").convert_alpha(),
                         pygame.image.load("Imgs\\fourPlayersChoose.png").convert_alpha()]

        twoButton = pygame.Rect(300, 400, 183, 80)
        threeButton = pygame.Rect(525, 400, 183, 80)
        fourButton = pygame.Rect(750, 400, 183, 80)

        while running:

            twoButtonHover = False
            threeButtonHover = False
            fourButtonHover = False

            click = False
            for event in pygame.event.get():  # check events here
                if event.type == QUIT:  # leave application
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse click
                    click = True

            mx, my = pygame.mouse.get_pos()
            if twoButton.collidepoint((mx, my)):
                twoButtonHover = True
                if click:
                    self.connect_menu(2)
                    running = False
            elif threeButton.collidepoint((mx, my)):
                threeButtonHover = True
                if click:
                    self.connect_menu(3)
                    running = False
            elif fourButton.collidepoint((mx, my)):
                fourButtonHover = True
                if click:
                    self.connect_menu(4)
                    running = False

            if running:  # tal vez ocupe agregar un blit al fondo
                self.screen.blit(twoButtonImg[1 if twoButtonHover else 0], [300, 400])
                self.screen.blit(threeButtonImg[1 if threeButtonHover else 0], [525, 400])
                self.screen.blit(fourButtonImg[1 if fourButtonHover else 0], [750, 400])

                pygame.display.flip()
                self.clock.tick(14)

    def main_menu(self):
        """
        Muestra el fondo inicial y le permite al jugador escoger si va a jugar
        Authors: Mariana
        :return:
        """
        running = True
        backgroundImg = [pygame.image.load("Imgs\\Bg1.png").convert(), pygame.image.load("Imgs\\Bg2.png").convert(),
                         pygame.image.load("Imgs\\Bg3.png").convert(), pygame.image.load("Imgs\\Bg4.png").convert(),
                         pygame.image.load("Imgs\\Bg5.png").convert(), pygame.image.load("Imgs\\Bg6.png").convert(),
                         pygame.image.load("Imgs\\Bg7.png").convert(), pygame.image.load("Imgs\\Bg8.png").convert()]
        logoImg = pygame.image.load("Imgs\\Logo.png").convert_alpha()
        playButtonImg = pygame.image.load("Imgs\\playButton.png").convert_alpha()
        playButtonOnImg = pygame.image.load("Imgs\\playButtonOn.png").convert_alpha()

        playButton = pygame.Rect(540, 306, 170, 100)

        bgFrame = 0

        while running:

            click = False
            for event in pygame.event.get():  # check events here
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):  # leave application
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # check for left mouse click
                    click = True

            mx, my = pygame.mouse.get_pos()

            playButtonHover = False
            if playButton.collidepoint((mx, my)):
                playButtonHover = True
                if click:
                    self.choose_menu()

            bgFrame = (0 if bgFrame >= 7 else bgFrame + 1)

            if running:
                self.screen.blit(backgroundImg[bgFrame], [0, 0])
                self.screen.blit(logoImg, [290, -20])
                self.screen.blit(playButtonOnImg if playButtonHover else playButtonImg, [510, 305])

                pygame.display.flip()
                self.clock.tick(14)

    def draw_text(self, text, font, color, surface, x, y):
        """
        Dibuja en el fondo inicial el texto 
        Author: Ignacio
        :param text:
        :param font:
        :param color:
        :param surface:
        :param x:
        :param y:
        :return:
        Restrictions: text must be string, font must be pygame font object
        """

        if text == "":
            return
        text = font.render(text, 1, color)
        surface.blit(text, (x, y))


play = Menu()
