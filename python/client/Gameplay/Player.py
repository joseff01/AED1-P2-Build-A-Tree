import pygame


class player(object):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, 50,
                                50)  # la idea es eventualmente cambiar esto con image.get_rect() cuando hayan sprites, por eso las llamadas en #position

        # position
        self.rect.x = x
        self.rect.y = y

        # movement
        self.speed_x = 5  # esta es constante
        self.speed_y = 0  # esta varía
        self.left = False
        self.right = False
        self.rising = False
        self.falling = False

    def move(self, left, right):
        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        platformsList=[leftCroc,rightBirb,leftStand,rightStand]

        if left:
            self.rect -= self.speed_x
        if right:
            self.rect += self.speed_x

        if self.rect.colliderect(land):
            if left:
                self.rect.right = land.left
            elif right:
                self.rect.left = land.right

        insidePlatform = self.rect.collidelist(platformsList)
        self.rect += self.speed_y

    def jump(self):
        return

    def colision(self, who):

        while who.colFrames <= 9:
            if self.x < who.x:
                who.move(1)
            else:
                who.move(2)
            who.colFrames += 1

        who.colFrames = 0
