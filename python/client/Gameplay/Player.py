import pygame


class Player(object):
    def __init__(self, x, y, width, height,skin):
        self.rect = pygame.Rect(x, y, width, height)
        # la idea es eventualmente cambiar esto con image.get_rect() cuando hayan sprites, por eso las llamadas en #position

        # position
        self.rect.x = x
        self.rect.y = y

        # movement
        self.speed_x = 9  # esta es constante
        self.speed_y = 0  # esta varía
        self.left = False
        self.right = False
        self.rising = False
        self.falling = False
        self.push = False
        self.moveRight = False
        self.count = 10
        self.moveCount = 0
        self.fallingCount = 0

        #poderes
        self.forcePush = False
        self.doubleJump = False
        self.shield = False
        self.clock = 0
        self.clockStart = 0

        #arbol
        self.tree = None

    def move(self, playersList):
        land = pygame.Rect(283, 468, 635, 210)
        leftCroc = pygame.Rect(300, 373, 105, 20)
        leftStand = pygame.Rect(485, 300, 76, 10)
        rightStand = pygame.Rect(639, 300, 76, 10)
        rightBirb = pygame.Rect(795, 373, 105, 20)
        bottomland = pygame.Rect(0, 750, 1500, 1)
        platformsList = [land, leftCroc, rightBirb, leftStand, rightStand,bottomland]

        # Push
        if self.count <= 0:
            self.count = 10
            self.push = False
            self.moveRight = False

        if self.push == True and self.moveRight:
            self.count -= 1
            self.rect.x +=(self.count**2)*0.5

        if self.push == True and self.moveRight == False:
            self.count -= 1
            self.rect.x -=(self.count**2)*0.5

        # mover horizontal
        if self.left:
            self.rect.x -= self.speed_x
        if self.right:
            self.rect.x += self.speed_x

        # Revisar si pegó con la tierra
        if self.rect.colliderect(land) and self.rect.bottom > land.top + 50:  # ///// Aquí el land.top+n lo tiene que ajustar para que sea como el piso máximo de los maecitos
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
                if self.rect.colliderect(bottomland):
                    self.rect.bottom = land.top
                    self.rect.x = 750
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

        self.collide(playersList)

    def collide(self,playersList):
        for p in playersList:
            if self.rect.colliderect(p) and p.rect.x > self.rect.x:
                # force push power
                if self.right == True and self.forcePush:
                    p.count +=2
                    self.forcePush = False
                if p.left == True and p.forcePush:
                    self.count +=2
                    p.forcePush = False

                # Collisions
                if p.shield == False:
                    if self.right == True and p.left == False:
                        p.push = True
                        p.moveRight = True
                    if self.right == True and p.left == True:
                        p.push = True
                        p.moveRight = True
                        self.push = True
                if p.clock == 0:
                    p.clock = pygame.time.get_ticks() // 1000
                    p.clockStart = pygame.time.get_ticks() // 1000
                else:
                    p.clock = pygame.time.get_ticks() // 1000
                    if p.clock - p.clockStart>= 8:
                        p.clock = 0
                        p.clockStart = 0
                        p.shield = False

                if self.shield == False:
                    if self.right == False and p.left == True:
                        self.push = True
                if self.clock == 0:
                    self.clock = pygame.time.get_ticks() // 1000
                    self.clockStart = pygame.time.get_ticks() // 1000
                else:
                    self.clock = pygame.time.get_ticks() // 1000
                    if self.clock - p.clockStart>= 8:
                        self.clock = 0
                        self.clockStart = 0
                        self.shield = False

    def jump(self):
        if (self.falling or self.rising) and self.doubleJump:
            self.speed_y = -20  # //////Aquí se cambia la velocidad incial cuando se salta//////
            self.fallin = False
            self.rising = True
            self.doubleJump = False

        if not self.falling and not self.rising:
            self.speed_y = -20  # //////Aquí se cambia la velocidad incial cuando se salta//////
            self.rising = True

    def setMoveCount(self,moveCount):
        self.moveCount = moveCount

    def setfallingCount(self,fallingCount):
        self.fallingCount = fallingCount

    def setForcePush(self,boolean):
        self.forcePush = boolean

    def setDoubleJump(self,boolean):
        self.doubleJump = boolean

    def setShield(self,boolean):
        self.shield = boolean




