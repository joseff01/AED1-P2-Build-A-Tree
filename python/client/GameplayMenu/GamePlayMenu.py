import pygame, threading

from python.client.GameplayMenu.Player import player

frame = 0


class gameplay:
    def __init__(self, screen, s, num):
        dead = False

        background_image = [pygame.image.load("Imgs\\GamePlay\\bgGame0.png"), pygame.image.load("Imgs\\GamePlay\\bgGame1.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame2.png"), pygame.image.load("Imgs\\GamePlay\\bgGame3.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame4.png"), pygame.image.load("Imgs\\GamePlay\\bgGame5.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame6.png"), pygame.image.load("Imgs\\GamePlay\\bgGame7.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame8.png"), pygame.image.load("Imgs\\GamePlay\\bgGame9.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame10.png"), pygame.image.load("Imgs\\GamePlay\\bgGame11.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame12.png"), pygame.image.load("Imgs\\GamePlay\\bgGame13.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame14.png"), pygame.image.load("Imgs\\GamePlay\\bgGame15.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame16.png"), pygame.image.load("Imgs\\GamePlay\\bgGame17.png"),
                            pygame.image.load("Imgs\\GamePlay\\bgGame18.png"), pygame.image.load("Imgs\\GamePlay\\bgGame19.png")]

        if num == 2 or num == 3 or num == 4:
            player1 = player(325, 415, 50, 50)
            player2 = player(850, 415, 50, 50)
            if num == 3:
                player3 = player(496, 250, 50, 50)
            elif num == 4:
                player3 = player(496, 255, 50, 50)
                player4 = player(650, 257, 50, 50)


        def checkColision():

            if recPlayer1.colliderect(recPlayer2) and (player1.pressed == True and player2.pressed ==False):
                player1.colision(player2)
            elif recPlayer2.colliderect(recPlayer1) and (player2.pressed == True and player1.pressed ==False):
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


            pygame.display.update()


        def spawnBichito(num):

            leftCroc = pygame.Rect(300, 373, 105, 20)

            pygame.draw.rect(screen, (100, 0, 0), leftCroc)
            pygame.draw.rect(screen, (100, 0, 0), recPlayer1)
            pygame.draw.rect(screen, (100, 0, 0), recPlayer2)
            if num == 3:
                pygame.draw.rect(screen, (100, 0, 0), [player3.x, player3.y, 50, 50])
            elif num == 4:
                pygame.draw.rect(screen, (100, 0, 0), [player3.x, player3.y, 50, 50])
                pygame.draw.rect(screen, (100, 0, 0), [player4.x, player4.y, 50, 50])
            checkColision()



        def setBackground():
            global frame
            screen.blit(background_image[frame], [0, 0])
            frame += 1
            if frame >= 19:
                frame = 0

        def receiveMessage():
            while (dead == False):
                messageJSON = s.recv(1024)
                print(messageJSON)

        receiveMessagesThread = threading.Thread(target=receiveMessage)
        receiveMessagesThread.start()

        def checkPressed():
            if (keys[ord('d')] or keys[ord('a')] or keys[ord('w')]) and player1.pressed == False:
                player1.pressed = True

            if (keys[ord('f')] or keys[ord('h')] or keys[ord('t')]) and player2.pressed == False:
                player2.pressed = True
            if num == 3 or num == 4:
                if (keys[ord('j')] or keys[ord('l')] or keys[ord('i')]) and player3.pressed == False:
                    player3.pressed = True
                if num ==4:
                    if (keys[ord('c')] or keys[ord('b')] or keys[ord('g')]) and player4.pressed == False:
                        player4.pressed = True



        while (dead == False):
            # Recibe los mensajes del servidor
            # messageJSON = s.recv(1024)
            # print(messageJSON)
            #################################
            pygame.time.delay(85)
            setBackground()
            keys = pygame.key.get_pressed()

            checkPressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    dead = True
                    receiveMessagesThread.join()
                if pygame.key.get_pressed():
                    if (not keys[ord('d')] or not keys[ord('a')]) and player1.pressed == True and player1.isJump == False:
                        player1.pressed = False
                    if (not keys[ord('f')] or not keys[ord('h')]) and player2.pressed == True and player2.isJump == False:
                        player2.pressed = False
                    if num == 3 or num == 4:
                        if (not keys[ord('j')] or not keys[ord('l')]) and player3.pressed == True and player3.isJump == False:
                            player3.pressed = False
                        if num == 4:
                            if (not keys[ord('c')] or not keys[ord('b')]) and player4.pressed == True and player4.isJump == False:
                                player4.pressed = False


            #colisiones
            recPlayer1 = pygame.Rect(player1.x, player1.y, 50, 50)
            recPlayer2 = pygame.Rect(player2.x, player2.y, 50, 50)

            if num == 3 or num ==4:
                recPlayer3 = pygame.Rect(player3.x, player3.y, 50, 50)
                if num == 4:
                    recPlayer4 = pygame.Rect(player4.x, player4.y, 50, 50)

            if not(recPlayer1.colliderect(recPlayer2) and (player1.pressed == True and player2.pressed ==True)):
                # moveplayer 1
                if player1.cae == False:
                    if keys[ord('d')]:
                        player1.move(1)
                    if keys[ord('a')]:
                        player1.move(2)
                    if not player1.isJump:
                        if keys[ord('w')]:
                            player1.isJump = True
                    else:
                        player1.move(3)
                else:
                    player1.move(0)

                # move player 2
                if player2.cae == False:
                    if keys[ord('h')]:
                        player2.move(1)
                    if keys[ord('f')]:
                        player2.move(2)
                    if not player2.isJump:
                         if keys[ord('t')]:
                            player2.isJump = True
                    else:
                        player2.move(3)
                else:
                    player2.move(0)
            else:
                if keys[ord('d')] and keys[ord('f')]:
                    player1.x -= 5
                    player2.x += 5
                else:
                    player1.x += 5
                    player2.x -= 5


            # move player 3  & 4
            if num == 3 or num == 4:
                if not ((recPlayer3.colliderect(recPlayer1) and (player3.pressed == True and player1.pressed == True)) or (recPlayer3.colliderect(recPlayer2) and (player3.pressed == True and player2.pressed == True))):
                    if player3.cae == False:
                        if keys[ord('l')]:
                            player3.move(1)
                        if keys[ord('j')]:
                            player3.move(2)
                        if not player3.isJump:
                            if keys[ord('i')]:
                                player3.isJump = True
                        else:
                            player3.move(3)
                    else:
                        player3.move(0)
                    if num == 4:
                        if not ((recPlayer4.colliderect(recPlayer1) and (player4.pressed == True and player1.pressed == True)) or (recPlayer4.colliderect(recPlayer2) and (player4.pressed == True and player2.pressed == True)) or (recPlayer4.colliderect(recPlayer3) and (player4.pressed == True and player3.pressed == True))):
                            if player4.cae == False:
                                if keys[ord('b')]:
                                    player4.move(1)
                                if keys[ord('c')]:
                                    player4.move(2)
                                if not player4.isJump:
                                    if keys[ord('g')]:
                                        player4.isJump = True
                                else:
                                    player4.move(3)
                            else:
                                player4.move(0)
                        else:
                            if keys[ord('c')] and keys[ord('d')]:
                                player1.x -= 5
                                player4.x += 5
                            elif keys[ord('c')] and keys[ord('h')]:
                                player2.x -= 5
                                player4.x += 5
                            elif keys[ord('c')] and keys[ord('l')]:
                                player3.x -= 15
                                player4.x += 5
                            elif keys[ord('b')] and keys[ord('a')]:
                                player4.x -= 5
                                player1.x += 5
                            elif keys[ord('b')] and keys[ord('f')]:
                                player4.x -= 5
                                player2.x += 5
                            else:
                                player4.x -= 5
                                player3.x += 5

                else:
                    if keys[ord('j')] and keys[ord('d')]:
                        player1.x -= 5
                        player3.x += 5
                    elif keys[ord('j')] and keys[ord('h')]:
                        player2.x -= 5
                        player3.x += 5
                    elif keys[ord('l')] and keys[ord('a')]:
                        player3.x -= 5
                        player1.x += 5
                    else:
                        player3.x += 5
                        player2.x -= 5

            spawnBichito(num)
