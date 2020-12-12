import random

import pygame


class PowerUps(object):
    def __init__(self,number):
        """
        mueve los objetos que asignan poderes y verifica que jugador colisiona con el objeto de poder.
        Authors: Mariana
        :param number:
        Restrictions: number must be an int
        """
        x = random.randint(30, 1200 - 30)
        self.rect = pygame.Rect(x, 0, 40, 40)
        self.count = 0
        self.type = number


    def setCount(self,count):
        """
        Cambia el valor de count
        Author: Mariana
        :param count:
        :return:
        Restictions: count must be int
        """
        self.count = count


    def fall(self,powerUpsList):
        """
        Mueve los objetos hacia abajo, verifica si el objeto colisiona con las plataformas
        Author: Mariana
        :param powerUpsList:
        :return:
        Restrictions: powerUpsList must be a list
        """
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
        """
        Elimina powerUpsList el objeto de la lista
        Authors: Mariana
        :param powerUpsList:
        :return:
        Restrictions: powerUpsList must be a list
        """
        if self in powerUpsList:
            powerUpsList.remove(self)

    def catchCheck(self, playersList):
        """
        Verifica si el objeto colisiona con los jugadores
        :param playersList:
        :return:
        Restrictions: playersList must be a list
        """
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



