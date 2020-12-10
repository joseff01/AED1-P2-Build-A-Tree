import random
import pygame


class Node:
    def __init__(self, node_type, number):
        x = random.randint(30, 1200 - 30)

        self.rect = pygame.Rect(x, 0, 20, 20)

        self.type = node_type
        self.number = number
        self.receiver = 0
        self.speed_y = 10

    def fall(self, nodesList):
        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        platformsList = [land, leftCroc, rightBirb, leftStand, rightStand]

        self.rect.y += self.speed_y

        # si toca plataforma
        if self.rect.collidelist(platformsList) != -1:
            self.delete(nodesList)

    def draw(self, surface):
        borderWidth = 2
        WHITE = (255, 255, 255)
        BLUE = (32, 28, 176)
        RED = (171, 10, 10)
        GREEN = (1, 135, 6)
        YELLOW = (235, 192, 52)
        if self.type == "BSTToken":  # red square
            pygame.draw.rect(surface, RED, self.rect)
            pygame.draw.rect(surface, WHITE, self.rect, borderWidth)
        elif self.type == "AVLToken":  # blue hexagon
            x = self.rect.x
            y = self.rect.y
            hexagonPoints = [(x + self.rect.width / 3, y), (x + 2 * self.rect.width / 3, y),  # Puntos arriba
                             (self.rect.right, + self.rect.height / 3), (self.rect.right, y + 2 * self.rect.height / 3),
                             # Puntos derecha
                             (x + 2 * self.rect.width / 3, self.rect.bottom),
                             (x + self.rect.width / 3, self.rect.bottom),  # Puntos abajo
                             (x, y + 2 * self.rect.height / 3), (x, y + self.rect.height / 3)]  # Puntos izquierda
            pygame.draw.polygon(surface, BLUE, hexagonPoints)
            pygame.draw.polygon(surface, WHITE, hexagonPoints, borderWidth)
        elif self.type == "BToken":  # yellow circle
            pygame.draw.circle(surface, YELLOW, self.rect.center, self.rect.width/2)
            pygame.draw.circle(surface, WHITE, self.rect.center, self.rect.width/2, borderWidth)
        elif self.type == "SplayToken":  # green tringle
            trianglePoints = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
            pygame.draw.polygon(surface, GREEN, trianglePoints)
            pygame.draw.polygon(surface, WHITE, trianglePoints, borderWidth)

    def delete(self, nodesList):
        nodesList.remove(self)


def draw_text(text, font, color, surface, x, y):
    """
    :param text: string that wants to be drawn
    :param font: font to draw with
    :param color: color of text
    :param surface: surface to draw text in
    :param x: coordinate x
    :param y: coordinate y
    :return: None
    """

    if text == "":
        return
    text = font.render(text, 1, color)
    surface.blit(text, (x, y))
