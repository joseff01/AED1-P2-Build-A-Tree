import random

import pygame


class PowerUps(object):
    def __init__(self,number):
        x = random.randint(30, 1200 - 30)

        self.rect = pygame.Rect(x, 0, 40, 40)
        self.count = 0
        self.type = number


    def setCount(self,count):
        self.count = count


    def fall(self,powerUpsList):
        land = pygame.Rect(283, 468, 635, 210)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        bottomland = pygame.Rect(0, 750, 1500, 1)
        platformsList = [land, leftCroc, rightBirb, leftStand, rightStand, bottomland]

        self.rect.y += 5

        if self.rect.collidelist(platformsList) != -1 or self.rect.y > 674:
            self.deletePow(powerUpsList)

    def deletePow(self, powerUpsList):
        if self in powerUpsList:
            powerUpsList.remove(self)

    def catchCheck(self, playersList):
        for player in playersList:
            if self.rect.colliderect(player.rect):
                if self.type == 1:
                    player.setDoubleJump(True)
                if self.type == 2:
                    player.setShield(True)
                if self.type == 3:
                    player.setForcePush(True)
                return True
        return False



