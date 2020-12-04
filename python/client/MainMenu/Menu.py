from time import sleep

from python.client.GameplayMenu.GamePlayMenu import gameplay
import pygame, socket, sys
from pygame.locals import *

pygame.init()


class Menu:

    def __init__(self):

        self.screen = pygame.display.set_mode((1200, 674))
        self.clock = pygame.time.Clock

        IpString = ""
        SocketString = ""
        IpRect = pygame.Rect(550, 200, 400, 50)
        SocketRect = pygame.Rect(550, 300, 400, 50)
        color = pygame.Color("white")
        copperplateFont = pygame.font.SysFont("copperplate gothic", 32)
        IpActive = False
        SocketActive = False

        run = True
        setServerSettingFlag = False
        frame = 0

        screen = self.screen

        pygame.display.set_caption("Smash Bros")

        background_image = [pygame.image.load("Imgs\\Bg1.png").convert(), pygame.image.load("Imgs\\Bg2.png").convert(),
                            pygame.image.load("Imgs\\Bg3.png").convert(), pygame.image.load("Imgs\\Bg4.png").convert(),
                            pygame.image.load("Imgs\\Bg5.png").convert(), pygame.image.load("Imgs\\Bg6.png").convert(),
                            pygame.image.load("Imgs\\Bg7.png").convert(), pygame.image.load("Imgs\\Bg8.png").convert()]

        rec = pygame.Rect(540, 306, 170, 100)
        rec1 = pygame.Rect(300, 400, 183, 80)
        rec2 = pygame.Rect(525, 400, 183, 80)
        rec3 = pygame.Rect(750, 400, 183, 80)

        choose = False
        num = 0
        click = False

        s = None

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    sleep(0.1)
                    click = True
                    if IpRect.collidepoint(event.pos):
                        IpActive = True
                        SocketActive = False
                    elif SocketRect.collidepoint(event.pos):
                        IpActive = False
                        SocketActive = True
                    else:
                        IpActive = False
                        SocketActive = False
                if event.type == pygame.MOUSEBUTTONUP:
                    click = False
                if (event.type == pygame.KEYDOWN):
                    if event.key == pygame.K_RETURN:
                        if (IpString == "127.0.0.1" or IpString.upper() == "LOCALHOST"):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.connect(("127.0.0.1", int(SocketString)))
                                sleep(0.5)
                                s.send("Start Server Connection\n".encode())
                                run = False
                                print(num)
                                gameplay(screen, s, num)
                            except:
                                print("Could not connect to Server, try another socket or IP")

                    if IpActive:
                        if event.key == pygame.K_BACKSPACE:
                            IpString = IpString[:-1]
                        elif len(IpString) < 18:
                            IpString += event.unicode
                    elif SocketActive:
                        if event.key == pygame.K_BACKSPACE:
                            SocketString = SocketString[:-1]
                        elif len(SocketString) < 5:
                            SocketString += event.unicode

            screen.blit(background_image[frame], [0, 0])

            if not setServerSettingFlag:
                screen.blit(pygame.image.load("Imgs\\Logo.png"), [290, -20])

            frame += 1

            if frame >= 8:
                frame = 0

            if not setServerSettingFlag:
                if rec.collidepoint(pygame.mouse.get_pos()) and click == True:
                    choose = True
                elif rec.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(pygame.image.load("Imgs\\playButtonOn.png"), [510, 305])
                else:
                    screen.blit(pygame.image.load("Imgs\\playButton.png"), [510, 305])

            else:
                screen.blit(pygame.image.load("Imgs\\beforeImage2.png"), [0, 0])
                pygame.draw.rect(screen, color, IpRect)
                pygame.draw.rect(screen, color, SocketRect)
                IpLabelText = copperplateFont.render("Server Ip:", True, (0, 0, 0))
                SocketLabelText = copperplateFont.render("Server Socket:", True, (0, 0, 0))
                IpText = copperplateFont.render(IpString, True, (0, 0, 0))
                SocketText = copperplateFont.render(SocketString, True, (0, 0, 0))
                screen.blit(IpText, (IpRect.x + 5, IpRect.y + 5))
                screen.blit(SocketText, (SocketRect.x + 5, SocketRect.y + 5))
                screen.blit(IpLabelText, (IpRect.x - 190, IpRect.y + 10))
                screen.blit(SocketLabelText, (SocketRect.x - 290, SocketRect.y + 10))

            if choose:
                screen.blit(pygame.image.load("Imgs\\beforeImage.png"), [0, 0])
                if rec1.collidepoint(pygame.mouse.get_pos()) and click == True:
                    num = 2
                    setServerSettingFlag = True
                    choose = False
                elif rec2.collidepoint(pygame.mouse.get_pos()) and click == True:
                    num = 3
                    setServerSettingFlag = True
                    choose = False
                elif rec3.collidepoint(pygame.mouse.get_pos()) and click == True:
                    num = 4
                    setServerSettingFlag = True
                    choose = False
                elif rec1.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(pygame.image.load("Imgs\\twoPlayersChoose.png"), [300, 400])
                    screen.blit(pygame.image.load("Imgs\\threePlayers.png"), [525, 400])
                    screen.blit(pygame.image.load("Imgs\\fourPlayers.png"), [750, 400])
                elif rec2.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(pygame.image.load("Imgs\\threePlayersChoose.png"), [525, 400])
                    screen.blit(pygame.image.load("Imgs\\twoPlayers.png"), [300, 400])
                    screen.blit(pygame.image.load("Imgs\\fourPlayers.png"), [750, 400])
                elif rec3.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(pygame.image.load("Imgs\\fourPlayersChoose.png"), [750, 400])
                    screen.blit(pygame.image.load("Imgs\\threePlayers.png"), [525, 400])
                    screen.blit(pygame.image.load("Imgs\\twoPlayers.png"), [300, 400])
                else:
                    screen.blit(pygame.image.load("Imgs\\twoPlayers.png"), [300, 400])
                    screen.blit(pygame.image.load("Imgs\\threePlayers.png"), [525, 400])
                    screen.blit(pygame.image.load("Imgs\\fourPlayers.png"), [750, 400])

            sleep(0.1)
            pygame.display.update()

    def connect_menu(self, playerNum):
        running = True

        backgroundImg = pygame.image.load("Imgs\\beforeImage2.png").convert()
        copperplateFont = pygame.font.SysFont("copperplate gothic", 32)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)

        ipBox = pygame.Rect(550, 200, 400, 50)
        portBox = pygame.Rect(550, 300, 400, 50)

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
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
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
                                # sleep(0.5) why?
                                s.send("Start Server Connection\n".encode())
                                run = False
                                print(playerNum)
                                gameplay(self.screen, s, playerNum)
                            except:
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
                self.clock.tick(30)

    def choose_menu(self):
        running = True

        backgroundImg = pygame.image.load("Imgs\\beforeImage.png").convert()
        self.screen.blit(backgroundImg, [0, 0])

        # elemento 0 = apagado, 1 = encendido (Escogido)
        twoButtonImg = [pygame.image.load("Imgs\\twoPlayers.png").convert(),
                        pygame.image.load("Imgs\\twoPlayersChoose.png").convert()]
        threeButtonImg = [pygame.image.load("Imgs\\threePlayers.png").convert(),
                          pygame.image.load("Imgs\\threePlayersChoose.png").convert()]
        fourButtonImg = [pygame.image.load("Imgs\\fourPlayers.png").convert(),
                         pygame.image.load("Imgs\\fourPlayersChoose.png").convert()]

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
                self.clock.tick(30)

    def main_menu(self):
        running = True
        backgroundImg = [pygame.image.load("Imgs\\Bg1.png").convert(), pygame.image.load("Imgs\\Bg2.png").convert(),
                         pygame.image.load("Imgs\\Bg3.png").convert(), pygame.image.load("Imgs\\Bg4.png").convert(),
                         pygame.image.load("Imgs\\Bg5.png").convert(), pygame.image.load("Imgs\\Bg6.png").convert(),
                         pygame.image.load("Imgs\\Bg7.png").convert(), pygame.image.load("Imgs\\Bg8.png").convert()]
        logoImg = pygame.image.load("Imgs\\Logo.png").convert()
        playButtonImg = pygame.image.load("Imgs\\playButton.png").convert()
        playButtonOnImg = pygame.image.load("Imgs\\playButtonOn.png").convert()

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

            bgFrame = (0 if bgFrame >= 8 else bgFrame + 1)

            if running:
                self.screen.blit(backgroundImg[bgFrame], [0, 0])
                self.screen.blit(logoImg, [290, -20])
                self.screen.blit(playButtonOnImg if playButtonHover else playButtonImg, [510, 305])

                pygame.display.flip()
                self.clock.tick(30)

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


play = Menu()
