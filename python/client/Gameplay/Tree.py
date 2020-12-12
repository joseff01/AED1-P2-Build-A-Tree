import pygame
import math


class Tree:

    def __init__(self, treeDict):
        self.treeDict = treeDict
        self.type = treeDict['@type']
        if self.type == "BSTree" or self.type == "AVLTree":
            if treeDict['root'] is not None:
                self.height = treeDict['root']['height']
                if self.type == "AVLTree":
                    self.height -= 1
            else:
                self.height = 0
        elif self.type == "BTree" or self.type == "SplayTree":
            self.height = treeDict['height']  # BTree
        self.owner = treeDict['owner']
        self.order = None

    def draw(self, surface):
        treeArea = pygame.rect.Rect(1200 + 5, ((self.owner - 1) * 674 / 4) + 30, 290, 135)
        if self.type != "BTree":
            font = pygame.font.SysFont("Century Gothic", round(50 * math.exp(-self.height / 2.6)))  # Set font for trees
            self.draw_BinaryTree(surface, font, self.treeDict['root'], treeArea)
        else:
            font = pygame.font.SysFont("Century Gothic", round(20 * math.exp(-self.height / 2.6)))  # Set font for trees
            self.draw_BTree(surface, font, self.treeDict['root'], treeArea)

    def draw_BTree(self, surface, font, current, treeArea, levelHeight=0, maxWidth=0, x=0, height=0):
        if current is None or self.order is None:
            return
        if height == 0:
            levelHeight = treeArea.height / (self.height + 1)  # la altura de cada etapa del árbol
            maxWidth = treeArea.width / (self.order ** (self.height + 1))  # el ancho de los nodos al más bajo nivel
            x = treeArea.centerx - (maxWidth / 2)
        WHITE = (255, 255, 255)
        RED = (171, 10, 10)
        borderWidth = 1

        y = treeArea.y + height * levelHeight

        keysSize = len(current['keys'])
        if keysSize == 0:
            return

        # Dibujar nodos
        nodeWidth = (maxWidth / keysSize) * 0.9
        nodeHeight = levelHeight * 0.8
        node_x = x - keysSize * nodeWidth / 2

        for key in current['keys']:
            numberString = str(key) if key >= 10 else "0" + str(key)
            numberText = font.render(numberString, 1, WHITE)
            numberSize = font.size(numberString)
            pygame.draw.rect(surface, RED, (node_x, y, nodeWidth, nodeHeight))
            pygame.draw.rect(surface, WHITE, (node_x, y, nodeWidth, nodeHeight), borderWidth)
            surface.blit(numberText, (node_x + (nodeWidth - numberSize[0]) / 2, y + (nodeHeight - numberSize[1]) / 2))
            node_x += nodeWidth

        # Dibujar lineas entre nodos

        x_diff_order = (0.5 if self.order % 2 == 0 else 1) * 2 ** (self.height - height - 1)
        n = math.floor(self.order / 2) * -1
        i = 0
        for branch in current['branches']:
            if i == keysSize:
                n = math.floor(self.order / 2)
            if self.order % 2 == 0 and n == 0:
                n += 1
            new_x = x + n * x_diff_order * maxWidth
            self.draw_BTree(surface, font, branch, treeArea, levelHeight, maxWidth, new_x, height + 1)
            n += 1
            i += 1

    def draw_BinaryTree(self, surface, font, current, treeArea, x=0, height=0, levelHeight=0, levelWidth=0):
        if current is None:
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
            # dibujar nodo
            pygame.draw.circle(surface, YELLOW, (x + levelWidth / 2, y + nodeHeight / 2), nodeHeight / 2)
            pygame.draw.circle(surface, WHITE, (x + levelWidth / 2, y + nodeHeight / 2), nodeHeight / 2, borderWidth)
            # dibujar líneas hacia abajo
            surface.blit(numberText, (x + (levelWidth - numberSize[0]) / 2, y + (nodeHeight - numberSize[1]) / 2))
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
        self.draw_BinaryTree(surface, font, current['left'], treeArea, x - x_diff, height + 1, levelHeight, levelWidth)
        self.draw_BinaryTree(surface, font, current['right'], treeArea, x + x_diff, height + 1, levelHeight, levelWidth)

    def set_BTree_order(self, order):
        self.order = order
