import Tkinter as tk
import time
import math
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        #disc configuration
        self.discs = []
        self.discsLength = 7

        #tower configuration
        self.towersLocation = [[216, 219],[326, 219],[437, 219]]

        self.createWidgets()

    def start(self):
        t = Thread(target=self.moveDiscToTower, args=(self.discs[6], 2))
        t.start()

    def initializeDiscs(self):
        baseWidthDiameter = 100
        widthDiameter = baseWidthDiameter
        widthDiameterOffset = 10
        heightDiameter = 20

        xOffset = 5
        yOffset = 10

        x, y = self.towersLocation[1]
        x -= (baseWidthDiameter / 2)

        for i in range(0, self.discsLength):
            self.discs.append(self.createDisc(x, y, widthDiameter, heightDiameter))
            x += xOffset
            y -= yOffset
            widthDiameter -= widthDiameterOffset

    def createWidgets(self):
        self.canvas = tk.Canvas(self, height = 350, width = 600)
        self.canvas.grid(column = 0)

        self.startButton = tk.Button(self, text='Start',command=self.start)
        self.startButton.grid(column = 1)

        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid(column = 1)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row = 1, columnspan = 2)

        self.photo = tk.PhotoImage(file = './discs_base.gif')
        self.canvas.create_image(330,200, image=self.photo)

        self.canvas.bind('<Motion>', self.printCurrentCoords)

        self.initializeDiscs()


    def printCurrentCoords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.coordsLabelValue.set('x: {} y: {}'.format(x, y))

    def createDisc(self, x, y, width, height):
        x0 = x
        y0 = y
        x1 = x + width
        y1 = y + height

        disc = self.canvas.create_oval(x0, y0, x1, y1)
        return disc

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

            #self.canvas.update()
            time.sleep(0.025)

    def moveDiscToTower(self, disc, tower):
        discCurrentTower = 1
        discDestinationTower = tower
        #discDestinationPosition = len(tower) + 1
        discDestinationPosition = 1
        upLimit = 110
        discX0, discY0, discX1, discY1 = self.canvas.coords(disc)
        discWidth = discX1 - discX0
        towerX, towerY = self.towersLocation[tower]

        upAmount = int(discY0 - upLimit)
        moveAmount = int(math.fabs(towerX - discX0) - (discWidth / 2))
        moveDirection = 'right' if discCurrentTower < discDestinationTower else 'left'
        downAmount = towerY - upLimit

        self.moveDisc(disc, 'up', upAmount)
        self.moveDisc(disc, moveDirection, moveAmount)
        self.moveDisc(disc, 'down', downAmount)


app = Application()
app.master.title('Sample application')
app.mainloop()
