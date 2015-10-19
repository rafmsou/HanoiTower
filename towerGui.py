from tower import TowerPosition

class TowerGui(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.towers = []

        # tower configuration
        self.towersInitCoords = [185, 140]
        self.towersDistance = 150
        self.towerWidth = 14
        self.towerHeight = 120

    def initializeTowers(self):
        if self.canvas == None:
            return

        x0, y0 = self.towersInitCoords
        for i in range(0, 3):
            if i == 0:
                x0, y0, x1, y1 = x0, y0, (x0 + self.towerWidth), (y0 + self.towerHeight)
            else:
                x0, y0 = (x0 + self.towersDistance), y0
                x1, y1 = (x0 + self.towerWidth), (y0 + self.towerHeight)

            tower = self.canvas.create_rectangle(x0, y0, x1, y1, outline='black', fill='#E0E0E0', width=3)
            self.towers.append(tower)

    def getTowerBaseCoords(self, towerPosition):
        tower = self.towers[towerPosition.value]
        x0, y0, x1, y1 = self.canvas.coords(tower)
        x = x0
        y = y1

        #an offset to give a little space
        y -= 25
        #the center of the tower
        x += self.towerWidth / 2

        return x,y
