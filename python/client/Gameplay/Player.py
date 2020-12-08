import pygame


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # otras caracteristicas
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.colFrames = 0
        self.pressed = False
        self.cae = False

    def move(self, move):
        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 5)
        rightStand = pygame.Rect(639, 300, 76, 5)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        recPlayer = pygame.Rect(self.x, self.y, 50, 50)

        if move == 3:
            if self.jumpCount <= 4 and ((recPlayer.colliderect(leftCroc)) or (recPlayer.colliderect(rightBirb )) or (recPlayer.colliderect(leftStand )) or (recPlayer.colliderect(rightStand))):
                self.isJump = False
                self.pressed = False
                self.jumpCount = 10
            elif self.jumpCount >= -10:
                neg = +1
                if self.jumpCount < 0:
                    neg = 1
                self.y -= (self.jumpCount * 2) * neg
                self.jumpCount -= 1

            elif not (recPlayer.colliderect(land) or ((recPlayer.colliderect(leftCroc)) or (recPlayer.colliderect(rightBirb )) or (recPlayer.colliderect(leftStand)) or (recPlayer.colliderect(rightStand)))):
                self.y+=10
            else:
                self.isJump = False
                self.pressed = False
                self.jumpCount = 10

        elif move == 0:
            recPlayer2 = pygame.Rect(self.x, self.y, 50, 50)
            if not (recPlayer2.colliderect(land) or ((recPlayer.colliderect(leftCroc)) or (recPlayer.colliderect(rightBirb )) or (recPlayer.colliderect(leftStand )) or (recPlayer.colliderect(rightStand)))):
                self.y += 10
            else:
                self.cae = False

        else:
            if move == 1:
                self.x += 10
                recPlayer2 = pygame.Rect(self.x, self.y, 50, 50)
                if not (recPlayer2.colliderect(land) or ((recPlayer.colliderect(leftCroc)) or (recPlayer.colliderect(rightBirb )) or (recPlayer.colliderect(leftStand )) or (recPlayer.colliderect(rightStand)))) and self.isJump == False:
                    self.cae = True
            if move == 2:
                self.x -= 10
                recPlayer2 = pygame.Rect(self.x, self.y, 50, 50)
                if not (recPlayer2.colliderect(land) or ((recPlayer.colliderect(leftCroc)) or (recPlayer.colliderect(rightBirb )) or (recPlayer.colliderect(leftStand ))or (recPlayer.colliderect(rightStand)))) and self.isJump == False:
                    self.cae = True


    def colision(self, who):

        while who.colFrames <= 9:
            if self.x< who.x:
                who.move(1)
            else:
                who.move(2)
            who.colFrames +=1

        who.colFrames = 0


