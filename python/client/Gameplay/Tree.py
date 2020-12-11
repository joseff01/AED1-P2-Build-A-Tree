import pygame
import math


class Tree:

    def __init__(self, treeDict):
        self.treeDict = treeDict
        self.type = treeDict['@type']
        if self.type == "BSTree" or self.type == "AVLTree":
            if treeDict['root'] is not None:
                self.height = treeDict['root']['height']
            else:
                self.height = 0
        elif self.type == "BTree" or self.type == "SplayTree":
            self.height = treeDict['height']  # BTree
        self.owner = treeDict['owner']

    def draw(self, surface):
        font = pygame.font.SysFont("Century Gothic", round(50 * math.exp(-self.height / 2.6)))  # Set font for trees
        treeArea = pygame.rect.Rect(1200 + 5, ((self.owner - 1) * 674 / 4) + 30, 290, 135)
        if self.type != "BTree":
            current = self.treeDict['root']
            self.draw_BSTree(surface, font, self.treeDict['root'], treeArea)

        else:
            pass

    # Falta ajustarlo para que se dibujen las líneas entre los nodos y el nodo no tome to.do el espacio
    # BTrees van a manejarse en otra función
    # Falta que arreglen height de AVLs y Splays
    # Hacer font ajustarse a tamaño de node
    def draw_BSTree(self, surface, font, current, treeArea, x=0, height=0, levelHeight=0, levelWidth=0):
        if current == None:
            return
        # nota: height empieza en 0
        if height == 0:
            levelHeight = treeArea.height / (self.height + 1)  # la altura de cada etapa del árbol
            levelWidth = treeArea.width / (2 ** self.height)  # el ancho de los nodos al más bajo nivel
            x = treeArea.centerx - (levelWidth / 2)
        WHITE = (255, 255, 255)
        BLUE = (32, 28, 176)
        GREEN = (1, 135, 6)
        YELLOW = (235, 192, 52)
        borderWidth = 1
        nodeHeight = levelHeight * 0.8

        numberString = str(current['key']) if current['key'] >= 10 else "0" + str(current['key'])
        numberText = font.render(numberString, 1, WHITE)
        numberSize = font.size(numberString)

        y = treeArea.y + height * levelHeight
        if self.type == "BSTree":
            pygame.draw.circle(surface, YELLOW, (x + levelWidth / 2, y + nodeHeight / 2), nodeHeight / 2)
            pygame.draw.circle(surface, WHITE, (x + levelWidth / 2, y + nodeHeight / 2), nodeHeight / 2, borderWidth)
            surface.blit(numberText, (x + (levelWidth - numberSize[0]) / 2, y + (nodeHeight - numberSize[1]) / 2))
            # dibujar nodo
            # dibujar líneas hacia abajo
        elif self.type == "AVLTree":
            nodeWidth = nodeHeight
            hex_x = x + (levelWidth - nodeWidth) / 2
            hexagonPoints = [(hex_x + nodeWidth / 3, y), (hex_x + 2 * nodeWidth / 3, y),  # Puntos arriba
                             (hex_x + nodeWidth, y + nodeHeight / 3), (hex_x + nodeWidth, y + 2 * nodeHeight / 3),
                             # Puntos derecha
                             (hex_x + 2 * nodeWidth / 3, y + nodeHeight), (hex_x + nodeWidth / 3, y + nodeHeight),
                             # Puntos abajo
                             (hex_x, y + 2 * nodeHeight / 3), (hex_x, y + nodeHeight / 3)]  # Puntos izquierda
            pygame.draw.polygon(surface, BLUE, hexagonPoints)
            pygame.draw.polygon(surface, WHITE, hexagonPoints, borderWidth)
            surface.blit(numberText, (hex_x + (nodeWidth - numberSize[0]) / 2, y + (nodeHeight - numberSize[1]) / 2))
        elif self.type == "SplayTree":
            nodeWidth = nodeHeight
            tri_x = x + (levelWidth - nodeWidth) / 2
            trianglePoints = [(tri_x + nodeWidth / 2, y), (tri_x, y + nodeHeight), (tri_x + nodeWidth, y + nodeHeight)]
            pygame.draw.polygon(surface, GREEN, trianglePoints)
            pygame.draw.polygon(surface, WHITE, trianglePoints, borderWidth)
            surface.blit(numberText, (tri_x + (nodeWidth - numberSize[0]) / 2, y + nodeHeight - 5 * numberSize[1] / 6))

        x_diff = (1 / (2 ** (height + 2))) * treeArea.width
        if current['left'] is not None:
            pygame.draw.line(surface, WHITE, (x + levelWidth / 2, y + nodeHeight),
                             ((x + levelWidth / 2) - x_diff, y + levelHeight), borderWidth)
        if current['right'] is not None:
            pygame.draw.line(surface, WHITE, (x + levelWidth / 2, y + nodeHeight),
                             ((x + levelWidth / 2) + x_diff, y + levelHeight), borderWidth)
        self.draw_BSTree(surface, font, current['left'], treeArea, x - x_diff, height + 1, levelHeight, levelWidth)
        self.draw_BSTree(surface, font, current['right'], treeArea, x + x_diff, height + 1, levelHeight, levelWidth)
