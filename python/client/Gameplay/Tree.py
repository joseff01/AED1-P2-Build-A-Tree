class Tree:
    def __init__(self, treeDict):
        self.treeDict = treeDict
        self.type = treeDict['@type']
        self.height = treeDict['root']['height']
        self.owner = treeDict['owner']

    def draw(self):
        base_x = 1200
        base_y = (self.owner) * 674 / 4
        return
