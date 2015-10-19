from disc import Disc
from tower import TowerPosition

class DiscGui(object):
    def __init__(self, canvas, towerGui):
        self.canvas = canvas
        self.towerGui = towerGui

        # disc configuration
        self.discs = []
        self.discsLength = 7
        self.discsColor = ['#9D9D9D','#E0E0E0']
        self.baseWidthDiameter = 120
        self.widthDiameter = self.baseWidthDiameter
        self.widthDiameterOffset = 10
        self.heightDiameter = 20


    def createDisc(self, index, x, y, width, height):
        x0 = x
        y0 = y
        x1 = x + width
        y1 = y + height

        colorFill = self.discsColor[index % 2]

        disc = self.canvas.create_oval(x0, y0, x1, y1, outline='black', fill=colorFill, width=3)
        return Disc(disc, index)

    def initializeDiscs(self):
        if self.canvas == None:
            return

        xOffset = 5
        yOffset = 10

        x, y = self.towerGui.getTowerBaseCoords(TowerPosition.Center)
        x -= (self.baseWidthDiameter / 2)

        for i in reversed(range(0, self.discsLength)):
            #disc index is not zero based, that's why '(i + 1)' below
            disc = self.createDisc((i + 1), x, y, self.widthDiameter, self.heightDiameter)
            self.discs.append(disc)
            x += xOffset
            y -= yOffset
            self.widthDiameter -= self.widthDiameterOffset
