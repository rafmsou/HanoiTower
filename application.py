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
        self.moveButton.grid(row=1, column=1, sticky=tk.E)

        self.resetButton = tk.Button(self, text='Reiniciar', command=self.resetStage, width=10)
        self.resetButton.grid(row=2, column=1, sticky=tk.E)

        self.stopButton = tk.Button(self, text='Parar', command=self.resetStage, width=10)
        self.stopButton.grid(row=3, column=1, sticky=tk.E)

        self.movementsValue = tk.StringVar()
        self.movementsLabel = tk.Label(self, textvariable=self.movementsValue)
        self.movementsLabel.grid(row=1, column=2, columnspan=2)

        self.addDisc = tk.Button(self, text='+ Disco', command=self.resetStage, width=10)
        self.addDisc.grid(row=2, column=2, sticky=tk.E)

        self.removeDisc = tk.Button(self, text='- Disco', command=self.resetStage, width=10)
        self.removeDisc.grid(row=3, column=2, sticky=tk.E)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row=4, column=3, columnspan=2)

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
        self.addDisc['state'] = 'disabled'
        self.removeDisc['state'] = 'disabled'
        
        self.hanoiGame.move()
        movs = self.hanoiGame.moveCount
        self.movementsValue.set('Movimentos: {}'.format(movs))
        self.after(5, self.solveAction)


app = Application()
app.master.title('Torre de Hanoi')
app.mainloop()
