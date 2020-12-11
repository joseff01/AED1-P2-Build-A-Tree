import pygame


class Tree:
    Font = None

    def __init__(self, treeDict):
        self.treeDict = treeDict
        self.type = treeDict['@type']
        if self.type != "BTree":
            self.height = treeDict['root']['height']
        self.owner = treeDict['owner']

    def draw(self, surface):
        treeArea = pygame.rect.Rect(1200 + 5, (self.owner * 674 / 4) + 30, 290, 135)
        if self.type != "BTree":
            current = self.treeDict['root']
            self.draw_BSTree(surface, self.treeDict['root'], treeArea)

        else:
            pass

    def draw_BSTree(self, surface, current, treeArea, x=0, height=0, levelHeight=0, levelWidth=0):
        if current == None:
            return
        # nota: height empieza en 0
        if height == 0:
            x = treeArea.centerx - (levelWidth / 2)
            levelHeight = treeArea.height / (self.height + 1)  # la altura de cada etapa del árbol
            levelWidth = treeArea.width / (2 ** self.height)  # el ancho de los nodos al más bajo nivel
        WHITE = (255, 255, 255)
        BLUE = (32, 28, 176)
        GREEN = (1, 135, 6)
        YELLOW = (235, 192, 52)
        borderWidth = 1
        numberText = self.Font.render(str(current['key']) if current['key'] >= 10 else "0" + str(current['key']), 1,
                                      WHITE)

        y = treeArea.y + height * levelHeight
        if self.type == "BSTree":
            pygame.draw.circle(surface, YELLOW, (x + levelWidth / 2, y + levelHeight / 2), levelHeight / 2)
            pygame.draw.circle(surface, WHITE, (x + levelWidth / 2, y + levelHeight / 2), levelHeight / 2, borderWidth)
            surface.blit(numberText, (x + levelWidth / 5, y + self.rect.height / 7))

            # dibujar nodo
            # dibujar líneas hacia abajo
        elif self.type == "AVLTree":
            hexagonPoints = [(x + levelWidth / 3, y), (x + 2 * levelWidth / 3, y),  # Puntos arriba
                             (x + levelWidth, y + levelHeight / 3), (x + levelWidth, y + 2 * levelHeight / 3),
                             # Puntos derecha
                             (x + 2 * levelWidth / 3, y + levelHeight), (x + levelWidth / 3, y + levelHeight),
                             # Puntos abajo
                             (x, y + 2 * levelHeight / 3), (x, y + levelHeight / 3)]  # Puntos izquierda
            pygame.draw.polygon(surface, BLUE, hexagonPoints)
            pygame.draw.polygon(surface, WHITE, hexagonPoints, borderWidth)
            surface.blit(numberText, (x + levelWidth / 5, y + levelHeight / 6))
        x_diff = (1 / (2 ** (height + 2))) * treeArea.width
        self.draw_BSTree(surface, current['left'], treeArea, x - x_diff, height + 1, levelHeight, levelWidth)
        self.draw_BSTree(surface, current['right'], treeArea, x + x_diff, height + 1, levelHeight, levelWidth)
