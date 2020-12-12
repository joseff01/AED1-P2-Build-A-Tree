import json
import random
import pygame


class Node:
    Font = None
    def __init__(self, node_type, number):
        """
        Mueve los nodos hacia abajo y verifica que jugador colisiona con el objeto de poder.
        Author: Ignacio
        :param node_type:
        :param number:
        Restrictions: node_type must be a string and number must an int
        """
        x = random.randint(30, 1200 - 30)

        self.rect = pygame.Rect(x, 0, 35, 35)

        self.type = node_type
        self.number = number
        self.receiver = 0
        self.speed_y = 6

    def fall(self, nodesList):
        """
        Mueve los nodos hacia abajo, Verifica si el objeto colisiona con las plataformas
        Author: Ignacio
        :param nodesList:
        :return:
        Restrictions: nodeList must be a list
        """
        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        extra = pygame.Rect(0, 0, 0, 0)
        platformsList = [land, leftCroc, rightBirb, leftStand, rightStand,extra]

        self.rect.y += self.speed_y

        # si toca plataforma
        if self.rect.collidelist(platformsList) != -1 or self.rect.y > 674:
            self.delete(nodesList)

    def check_catch(self, playersList):
        """
        Verifica si el nodo colisiona con el jugador
        Author: Ignacio
        :param playersList:
        :return:
        Restrictions: playersList must be a list
        """
        pNum = 1
        for player in playersList:
            if self.rect.colliderect(player.rect):
                self.receiver = pNum
                return True
            pNum += 1
        return False

    def draw(self, surface):
        """
        Dibuja los nodos en el window original
        Author: Ignacio
        :param surface:
        :return:
        """
        borderWidth = 2
        WHITE = (255, 255, 255)
        BLUE = (32, 28, 176)
        RED = (171, 10, 10)
        GREEN = (1, 135, 6)
        YELLOW = (235, 192, 52)
        x = self.rect.x
        y = self.rect.y
        numberText = self.Font.render(str(self.number) if self.number >= 10 else "0" + str(self.number), 1, WHITE)
        if self.type == "BSTToken":  # yellow circle
            pygame.draw.circle(surface, YELLOW, self.rect.center, self.rect.width / 2)
            pygame.draw.circle(surface, WHITE, self.rect.center, self.rect.width / 2, borderWidth)
            surface.blit(numberText, (x + self.rect.width / 5, y + self.rect.height / 7))
        elif self.type == "AVLToken":  # blue hexagon
            hexagonPoints = [(x + self.rect.width / 3, y), (x + 2 * self.rect.width / 3, y),  # Puntos arriba
                             (self.rect.right, y + self.rect.height / 3),
                             (self.rect.right, y + 2 * self.rect.height / 3),
                             # Puntos derecha
                             (x + 2 * self.rect.width / 3, self.rect.bottom),
                             (x + self.rect.width / 3, self.rect.bottom),  # Puntos abajo
                             (x, y + 2 * self.rect.height / 3), (x, y + self.rect.height / 3)]  # Puntos izquierda
            pygame.draw.polygon(surface, BLUE, hexagonPoints)
            pygame.draw.polygon(surface, WHITE, hexagonPoints, borderWidth)
            surface.blit(numberText, (x + self.rect.width / 5, y + self.rect.height / 6))
        elif self.type == "BToken":  # red square
            pygame.draw.rect(surface, RED, self.rect)
            pygame.draw.rect(surface, WHITE, self.rect, borderWidth)
            surface.blit(numberText, (x + self.rect.width / 5, y + self.rect.height / 6))
        elif self.type == "SplayToken":  # green tringle
            trianglePoints = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
            pygame.draw.polygon(surface, GREEN, trianglePoints)
            pygame.draw.polygon(surface, WHITE, trianglePoints, borderWidth)
            surface.blit(numberText, (x + self.rect.width / 4, y + 3 * self.rect.height / 8))

    def delete(self, nodesList):
        """
        Elimina el nodo de la lista
        Author: Ignacio
        :param nodesList:
        :return:
        Restrictions: nodeList must be a list
        """
        if self in nodesList:
            nodesList.remove(self)

    def send(self, socket):
        """
        Crea un Json y y envia un socket
        Authors: Ignacio
        :param socket:
        :return:
        Restrictions: socket must be a string
        """
        objectDict = {'@type': self.type, 'number': self.number, 'receiver': self.receiver}
        objectJSON = json.dumps(objectDict)
        socket.sendall((objectJSON + "\n").encode())
        return
