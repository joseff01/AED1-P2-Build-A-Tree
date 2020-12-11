import pygame


class Tree:
    def __init__(self, treeDict):
        self.treeDict = treeDict
        self.type = treeDict['@type']
        if self.type != "BTree":
            self.height = treeDict['root']['height']
        self.owner = treeDict['owner']

    def draw(self):
        treeArea = pygame.rect.Rect(1200 + 5, (self.owner * 674 / 4) + 30, 290, 135)
        base_x = 1200
        base_y = self.owner * 674 / 4
        if self.type != "BTree":
            current = self.treeDict['root']
            self.draw_BSTree(self.treeDict['root'], treeArea)

        else:
            pass

    def draw_BSTree(self, current, treeArea, x=0, height=0):
        if current == None:
            return
        #nota: height empieza en 0
        levelHeight = treeArea.height / (self.height+1)  # la altura de cada etapa del árbol
        levelWidth = treeArea.width/ (2^self.height) # el ancho de los nodos al más bajo nivel

        if height == 0:
            x = treeArea.centerx-(levelWidth/2)

        if self.type == "BSTree":


            # dibujar nodo
            # dibujar líneas hacia abajo
        x_diff=(1/(2^(height+2)))*treeArea.width
        self.draw_BSTree(current['left'], treeArea, x-x_diff, height + 1)
        self.draw_BSTree(current['right'], treeArea, x+x_diff, height + 1)
