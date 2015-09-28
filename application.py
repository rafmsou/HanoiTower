import Tkinter as tk
import time
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        #disc configuration
        self.discs = []
        self.discsLength = 7

        #tower configuration
        self.towersBasePoint = [[165, 219],[275, 219],[385, 219]]

        self.createWidgets()

    def initializeDiscs(self):
        baseWidthDiameter = 100
        widthDiameter = baseWidthDiameter
        widthDiameterOffset = 10
        heightDiameter = 20

        xOffset = 5
        yOffset = 10

        x, y = self.towersBasePoint[1]

        for i in range(0, self.discsLength):
            self.discs.append(self.create_disc(x, y, widthDiameter, heightDiameter))
            x += xOffset
            y -= yOffset
            widthDiameter -= widthDiameterOffset

    def createWidgets(self):
        self.canvas = tk.Canvas(self, height = 350, width = 600)
        self.canvas.grid(column = 0)
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid(column = 1)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row = 1, columnspan = 2)

        self.photo = tk.PhotoImage(file = './discs_base.gif')
        self.canvas.create_image(330,200, image=self.photo)

        self.canvas.bind('<Motion>', self.print_current_coords)

        self.initializeDiscs()

        #t = Thread(target=self.move_rect)
        #t.start()

    def print_current_coords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.coordsLabelValue.set('x: {} y: {}'.format(x, y))

    def create_disc(self, x, y, width, height):
        x0 = x
        y0 = y
        x1 = x + width
        y1 = y + height

        disc = self.canvas.create_oval(x0, y0, x1, y1)
        return disc

    def move_disc(self, disc, direction, amount):

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
            time.sleep(0.025)

app = Application()
app.master.title('Sample application')
app.mainloop()
