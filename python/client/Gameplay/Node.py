import random
import pygame


class Node:
    def __init__(self, node_type, number):
        self.x = random.randint(30, 1200 - 30)
        self.y = 0

        self.rect = pygame.Rect(self.x, self.y, 20, 20)

        self.type = node_type
        self.number = number
        self.receiver = 0
        self.speed_y = 10

    def fall(self):
        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        platformsList = [land, leftCroc, rightBirb, leftStand, rightStand]

        self.rect.y += self.speed_y

        # si toca plataforma
        if self.rect.collidelist(platformsList) != -1:
            self.delete()

    def draw(self, surface):
        width = 1
        WHITE = (255, 255, 255)
        BLUE = (32, 28, 176)
        RED = (171, 10, 10)
        GREEN = (1, 135, 6)
        YELLOW = (235, 192, 52)
        if self.type == "BSTToken":  # red square
            pygame.draw.rect(surface, RED, self.rect)
            pygame.draw.rect(surface, WHITE, self.rect, width)
        elif self.type == "AVLToken":  # blue hexagon
            hexagonPoints = [(self.x + self.rect.width / 3, self.y), (self.x + 2 * self.rect.width / 3, self.y),
                             # Puntos arriba
                             (self.rect.right, self.y + self.rect.height / 3),
                             (self.rect.right, self.y + 2 * self.rect.height / 3),  # Puntos derecha
                             (self.x + 2 * self.rect.width / 3, self.rect.bottom),
                             (self.x + self.rect.width / 3, self.rect.bottom),  # Puntos abajo
                             (self.x, self.y + 2 * self.rect.height / 3),
                             (self.x, self.y + self.rect.height / 3)]  # Puntos izquierda
            pygame.draw.polygon(surface, BLUE, hexagonPoints)
            pygame.draw.polygon(surface, BLUE, hexagonPoints, width)
        elif self.type == "BToken":  # yellow circle
            pygame.draw.circle(surface, YELLOW, self.rect.center, 20)
            pygame.draw.circle(surface, YELLOW, self.rect.center, 20, width)
        elif self.type == "SplayToken":  # green tringle
            trianglePoints = [self.rect.midtop, self.rect.bottomleft, self.rect.bottomright]
            self.rect = pygame.draw.polygon(surface, GREEN, trianglePoints)
            self.rect = pygame.draw.polygon(surface, GREEN, trianglePoints, width)

    def delete(self):
        pass


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
