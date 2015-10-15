import tkinter as tk
from hanoiGame import HanoiGame

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.resetButton = tk.Button(self, text='Reiniciar', command=self.resetStage, width=5)
        self.resetButton.grid(row=0, column=0)

        self.moveButton = tk.Button(self, text='Move', command=self.moveAction, width=5)
        self.moveButton.grid(row=0, column=1)

        self.coordsLabelValue = tk.StringVar()
        self.coordsLabel = tk.Label(self, textvariable=self.coordsLabelValue)
        self.coordsLabel.grid(row=2, columnspan=2)

        self.quitButton = tk.Button(self, text='Fechar',command=self.closeAction, width=5)
        self.quitButton.grid(row=3, column=1)

        self.resetStage()


    def resetStage(self):
        self.canvas = tk.Canvas(self, height=350, width=600)
        self.canvas.grid(row=1, column=0)
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
        self.moveButton['state'] = 'disabled'
        self.hanoiGame.move()
        self.moveButton['state'] = 'active'


    def closeAction(self):
        self.quit()

app = Application()
app.master.title('Torre de Hanoi')
app.mainloop()
