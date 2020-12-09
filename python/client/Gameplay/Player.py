import pygame


class player(object):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        # la idea es eventualmente cambiar esto con image.get_rect() cuando hayan sprites, por eso las llamadas en #position

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

    def move(self):
        land = pygame.Rect(283, 461, 635, 213)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        platformsList = [land, leftCroc, rightBirb, leftStand, rightStand]

        # mover horizontal
        if self.left:
            self.rect.x -= self.speed_x
        if self.right:
            self.rect.x += self.speed_x

        # revisar si pegó con la tierra
        if self.rect.colliderect(
                land) and self.rect.bottom > land.top + 50:  # ///// Aquí el land.top+n lo tiene que ajustar para que sea como el piso máximo de los maecitos
            if self.left:
                self.rect.left = land.right
            elif self.right:
                self.rect.right = land.left

        # revisar si está en medio de una plataforma (por si está saltando a través de una)
        insidePlatform = self.rect.collidelist(platformsList)
        # mover vertical
        if self.falling or self.rising:
            self.rect.y += self.speed_y
            for platform in platformsList:
                # si choca con una plataforma
                if self.rect.colliderect(platform):
                    # y específicamente está cayéndose y no es la plataforma que ya vimos por la que estaba pasando
                    if self.falling and platform is not platformsList[insidePlatform]:
                        self.rect.bottom = platform.top
                        self.speed_y = 0
                        self.falling = False

            # Manejar velocidad vertical
            if self.falling or self.rising:  # lo vuelvo a revisar porque pudo haber parado de estar falling al caer en una plataforma
                self.speed_y += 1  # /////Aquí se cambia la aceleración vertical del jugador//////
                if self.speed_y > 20:
                    self.speed_y = 20  # /////Aquí se cambia la velocidad máxima de caída/////
                if self.rising and self.speed_y > 0:  # aquí es si pasa de estar subiendo a estar cayendo
                    self.rising = False
                    self.falling = True

        # si se queda sin plataforma por debajo
        if self.falling == False and self.rising == False:
            self.falling = True
            tryoutRect = self.rect.copy()
            tryoutRect.y += 1
            for platform in platformsList:
                # si choca con una plataforma
                if tryoutRect.colliderect(platform):
                    self.falling = False

    def jump(self):
        if not self.falling and not self.rising:
            self.speed_y = -20  # //////Aquí se cambia la velocidad incial cuando se salta//////
            self.rising = True

    def colision(self, who):

        while who.colFrames <= 9:
            if self.x < who.x:
                who.move(1)
            else:
                who.move(2)
            who.colFrames += 1

        who.colFrames = 0