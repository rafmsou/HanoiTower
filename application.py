import tkinter as tk
from hanoiGame import HanoiGame
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.moveButton = tk.Button(self, text='Resolver', command=self.solveAction, width=10)
        self.moveButton.grid(row=1, column=2, sticky=tk.E)

        self.resetButton = tk.Button(self, text='Reiniciar', command=self.resetStage, width=10)
        self.resetButton.grid(row=2, column=2, sticky=tk.E)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row=3, columnspan=5)

        self.quitButton = tk.Button(self, text='Fechar',command=self.closeAction, width=10)
        self.quitButton.grid(row=4, column=4, sticky=tk.E)

        self.resetStage()


    def resetStage(self):
        self.canvas = tk.Canvas(self, height=350, width=600)
        self.canvas.grid(row=0, columnspan=5, sticky=tk.W)
        self.canvas.bind('<Motion>', self.printCurrentCoords)

        self.hanoiGame = HanoiGame(self.canvas)

    def printCurrentCoords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.coordsLabelValue.set('x: {} y: {}'.format(x, y))

    def solveAction(self):
        self.moveButton['state'] = 'disabled'
        self.hanoiGame.move()
        self.after(5, self.solveAction)

    def closeAction(self):
        self.quit()

app = Application()
app.master.title('Torre de Hanoi')
app.mainloop()
