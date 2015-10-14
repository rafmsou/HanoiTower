import tkinter as tk
from threading import Thread
from hanoiGame import HanoiGame

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.moveButton = tk.Button(self, text='Move', command=self.moveAction, width=5)
        self.moveButton.grid(row=0, column=1)

        self.canvas = tk.Canvas(self, height=350, width=600)
        self.canvas.grid(row=1, column=0)

        self.quitButton = tk.Button(self, text='Quit',command=self.quit, width=5)
        self.quitButton.grid(column=1)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row=2, columnspan=2)

        self.photo = tk.PhotoImage(file='./discs_base.gif')
        self.canvas.create_image(330,200, image=self.photo)

        self.canvas.bind('<Motion>', self.printCurrentCoords)

        self.hanoiGame = HanoiGame(self.canvas)
        self.hanoiGame.initializeDiscs()


    def printCurrentCoords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.coordsLabelValue.set('x: {} y: {}'.format(x, y))

    def moveAction(self):
        self.hanoiGame.move()


app = Application()
app.master.title('Sample application')
app.mainloop()
