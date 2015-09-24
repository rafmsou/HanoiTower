import Tkinter as tk
import time
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()

        #disc configuration
        self.discsLength = 7
        self.discWidthDiameterStart = 40
        self.discWidthDiameterOffset = 10
        self.discHeightDiameter = 20


        self.createWidgets()

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

        self.canvas.disc1 = self.create_disc(195, 130, 40, 20)
        self.canvas.disc2 = self.create_disc(190, 145, 50, 20)
        self.canvas.disc3 = self.create_disc(185, 160, 60, 20)
        self.canvas.disc4 = self.create_disc(180, 175, 70, 20)
        self.canvas.disc5 = self.create_disc(175, 190, 80, 20)
        self.canvas.disc6 = self.create_disc(170, 205, 90, 20)
        self.canvas.disc7 = self.create_disc(165, 220, 100, 20)

        self.canvas.disc11 = self.create_disc(305, 130, 40, 20)
        self.canvas.disc12 = self.create_disc(300, 145, 50, 20)
        self.canvas.disc13 = self.create_disc(295, 160, 60, 20)
        self.canvas.disc14 = self.create_disc(290, 175, 70, 20)
        self.canvas.disc15 = self.create_disc(285, 190, 80, 20)
        self.canvas.disc16 = self.create_disc(280, 205, 90, 20)
        self.canvas.disc17 = self.create_disc(275, 220, 100, 20)

        self.canvas.disc11 = self.create_disc(415, 130, 40, 20)
        self.canvas.disc12 = self.create_disc(410, 145, 50, 20)
        self.canvas.disc13 = self.create_disc(405, 160, 60, 20)
        self.canvas.disc14 = self.create_disc(400, 175, 70, 20)
        self.canvas.disc15 = self.create_disc(395, 190, 80, 20)
        self.canvas.disc16 = self.create_disc(390, 205, 90, 20)
        self.canvas.disc17 = self.create_disc(385, 220, 100, 20)

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

    def move_rect(self):
        for i in xrange(1, 100):
            self.canvas.move(o, -1, 0)
            self.canvas.update()
            time.sleep(0.025)
            self.quit()

app = Application()
app.master.title('Sample application')
app.mainloop()
