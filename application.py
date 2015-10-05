import Tkinter as tk
from threading import Thread
from hanoiGame import HanoiGame

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, height = 350, width = 600)
        self.canvas.grid(column = 0)

        self.startButton = tk.Button(self, text='Start')
        self.startButton.grid(column = 1)

        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid(column = 1)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row = 1, columnspan = 2)

        self.photo = tk.PhotoImage(file = './discs_base.gif')
        self.canvas.create_image(330,200, image=self.photo)

        self.canvas.bind('<Motion>', self.printCurrentCoords)

        self.hanoiGame = HanoiGame(self.canvas)
        self.hanoiGame.initializeDiscs()
        self.hanoiGame.move()
        self.hanoiGame.move()

    def printCurrentCoords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.coordsLabelValue.set('x: {} y: {}'.format(x, y))


app = Application()
app.master.title('Sample application')
app.mainloop()
