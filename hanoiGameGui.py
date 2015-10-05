import time, math
from discGui import DiscGui

class HanoiGameGui(object):

    def __init__(self, canvas):
        self.canvas = canvas

        #disc configuration
        self.discs = []
        self.discsLength = 7

        #tower configuration
        self.towersLocation = [[215, 219],[326, 219],[437, 219]]

    def initializeDiscs(self):
        baseWidthDiameter = 100
        widthDiameter = baseWidthDiameter
        widthDiameterOffset = 10
        heightDiameter = 20

        xOffset = 5
        yOffset = 10

        x, y = self.towersLocation[1]
        x -= (baseWidthDiameter / 2)

        for i in reversed(range(0, self.discsLength)):
            disc = self.createDisc(i, x, y, widthDiameter, heightDiameter)
            self.discs.append(disc)
            x += xOffset
            y -= yOffset
            widthDiameter -= widthDiameterOffset

    def createDisc(self, index, x, y, width, height):
        x0 = x
        y0 = y
        x1 = x + width
        y1 = y + height

        disc = self.canvas.create_oval(x0, y0, x1, y1)
        return DiscGui(disc, index)

    def moveDisc(self, disc, direction, amount):

        for i in xrange(1, amount):
            if direction == 'left':
                self.canvas.move(disc, -1, 0)
            elif direction == 'right':
                self.canvas.move(disc, 1, 0)
            elif direction == 'up':
                self.canvas.move(disc, 0, -1)
            elif direction == 'down':
                self.canvas.move(disc, 0, 1)

            self.canvas.update()
            time.sleep(0.001)

    def moveDiscToTower(self, disc, tower):

        # gets the disc GUI element from self.discs with the given index
        discGUI = [d for d in self.discs if d.index == (disc - 1)][0]

        discCurrentTower = discGUI.currentTower
        discDestinationTower = tower.index
        discDestinationPosition = len(tower) + 1
        moveUpLimit = 110
        discX0, discY0, discX1, discY1 = self.canvas.coords(discGUI.disc)
        discWidth = discX1 - discX0
        towerX, towerY = self.towersLocation[tower.index]

        upAmount = int(discY0 - moveUpLimit)
        moveDirection = 'right' if discCurrentTower < discDestinationTower else 'left'
        moveAmount = towerX - discX0
        moveAmount += (discWidth / 2) * -1
        moveAmount = int(math.fabs(moveAmount))

        baseToDestinationDistance = (discDestinationPosition -  1) * 10
        downAmount = (towerY - moveUpLimit) - baseToDestinationDistance

        self.moveDisc(discGUI.disc, 'up', upAmount)
        self.moveDisc(discGUI.disc, moveDirection, moveAmount)
        self.moveDisc(discGUI.disc, 'down', downAmount)

        discGUI.currentTower = discDestinationTower
