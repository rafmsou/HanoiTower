import math, time, queue, platform
from disc import Disc

class HanoiGameGui(object):

    def __init__(self, canvas):
        self.canvas = canvas

        # disc configuration
        self.discs = []
        self.discsLength = 7
        self.discsColor = ['#9D9D9D','#E0E0E0']

        # tower configuration
        self.towersLocation = [[214, 217],[326, 217],[437, 217]]

    def initializeDiscs(self):
        if self.canvas == None:
            return

        baseWidthDiameter = 120
        widthDiameter = baseWidthDiameter
        widthDiameterOffset = 10
        heightDiameter = 20

        xOffset = 5
        yOffset = 10

        x, y = self.towersLocation[1]
        x -= (baseWidthDiameter / 2)

        for i in reversed(range(0, self.discsLength)):
            #disc index is not zero based, that's why '(i + 1)' below
            disc = self.createDisc((i + 1), x, y, widthDiameter, heightDiameter)
            self.discs.append(disc)
            x += xOffset
            y -= yOffset
            widthDiameter -= widthDiameterOffset

    def createDisc(self, index, x, y, width, height):
        x0 = x
        y0 = y
        x1 = x + width
        y1 = y + height

        colorFill = self.discsColor[index % 2]

        disc = self.canvas.create_oval(x0, y0, x1, y1, outline='black', fill=colorFill, width=3)
        return Disc(disc, index)

    def moveDisc(self, disc, direction, amount):
        isWindows = self.isWindowsOS()

        m,i = 1,0
        while i < amount:
            if direction == 'left':
                self.canvas.move(disc, m*-1, 0)
            elif direction == 'right':
                self.canvas.move(disc, m, 0)
            elif direction == 'up':
                self.canvas.move(disc, 0, m*-1)
            elif direction == 'down':
                self.canvas.move(disc, 0, m)
            i += m

            if isWindows:
                time.sleep(0.001)

            if i % 10 == 0:
                self.canvas.update()


    def moveDiscToTower(self, disc, tower):
        if self.canvas == None:
            return

        # gets the disc GUI element from self.discs with the given index
        discObject = [d for d in self.discs if d.index == disc][0]

        discCurrentTower = discObject.currentTower
        discDestinationTower = tower.index
        discDestinationPosition = len(tower) + 1
        moveUpLimit = 110
        discX0, discY0, discX1, discY1 = self.canvas.coords(discObject.disc)
        discWidth = discX1 - discX0
        towerX, towerY = self.towersLocation[tower.index]

        upAmount = int(discY0 - moveUpLimit)
        moveDirection = 'right' if discCurrentTower < discDestinationTower else 'left'
        moveAmount = towerX - discX0
        moveAmount += (discWidth / 2) * -1
        moveAmount = int(math.fabs(moveAmount))

        baseToDestinationDistance = (discDestinationPosition -  1) * 10
        downAmount = (towerY - moveUpLimit) - baseToDestinationDistance

        self.moveDisc(discObject.disc, 'up', upAmount)
        self.moveDisc(discObject.disc, moveDirection, moveAmount)
        self.moveDisc(discObject.disc, 'down', downAmount)

        discObject.currentTower = discDestinationTower

    def isWindowsOS(self):
        if str.lower(platform.system()) == 'windows':
            return True

        return False
