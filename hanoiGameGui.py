import math, time, platform
from discGui import DiscGui
from towerGui import TowerGui

class HanoiGameGui(object):

    def __init__(self, canvas):
        self.canvas = canvas
        self.towerGui = TowerGui(self.canvas)
        self.towerGui.initializeTowers()
        self.discGui = DiscGui(self.canvas, self.towerGui)
        self.discGui.initializeDiscs()

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

        # gets the disc GUI element with the given index
        discObject = [d for d in self.discGui.discs if d.index == disc][0]

        discCurrentTower = discObject.currentTower
        discDestinationTower = tower.position.value
        discDestinationPosition = len(tower) + 1
        moveUpLimit = 110
        discX0, discY0, discX1, discY1 = self.canvas.coords(discObject.disc)
        discWidth = discX1 - discX0
        towerX, towerY = self.towerGui.getTowerBaseCoords(tower.position)

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
