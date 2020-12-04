from time import sleep

from python.client.GameplayMenu.GamePlayMenu import gameplay
import pygame, socket

pygame.init()


class MainMenu:
    def __init__(self):

        IpString = ""
        SocketString = ""
        IpRect = pygame.Rect(550, 200, 400, 50)
        SocketRect = pygame.Rect(550, 300, 400, 50)
        color = pygame.Color("white")
        copperplateFont = pygame.font.SysFont("copperplate gothic", 32)
        IpActive = False
        SocketActive = False

        run = False
        setServerSettingFlag = False
        frame = 0

        screen = pygame.display.set_mode((1200, 674))
        pygame.display.set_caption("Smash Bros")

        background_image = [pygame.image.load("Imgs\\Bg1.png"), pygame.image.load("Imgs\\Bg2.png"),
                            pygame.image.load("Imgs\\Bg3.png"), pygame.image.load("Imgs\\Bg4.png"),
                            pygame.image.load("Imgs\\Bg5.png"), pygame.image.load("Imgs\\Bg6.png"),
                            pygame.image.load("Imgs\\Bg7.png"), pygame.image.load("Imgs\\Bg8.png")]

        rec = pygame.Rect(540, 306, 170, 100)
        rec1 = pygame.Rect(300, 400, 183, 80)
        rec2 = pygame.Rect(525, 400, 183, 80)
        rec3 = pygame.Rect(750, 400, 183, 80)

        choose = False
        num = 0
        click = False

        s = None

        while not run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = True
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
                        if (IpString == "127.0.0.1"):
                            try:
                                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                s.connect(("127.0.0.1", int(SocketString)))
                                sleep(0.5)
                                s.send("Start Server Connection\n".encode())
                                run = True
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


play = MainMenu()
