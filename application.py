import Tkinter as tk
import time
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
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

        t = Thread(target=self.move_rect)
        t.start()

    def print_current_coords(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.coordsLabelValue.set('x: {} y: {}'.format(x, y))

    def move_rect(self):

        o = self.canvas.create_oval(170, 225, 250, 240)

        # for i in xrange(1, 100):
        #     self.canvas.move(o, -1, 0)
        #     self.canvas.update()
        #     time.sleep(0.025)self.quit()


app = Application()
app.master.title('Sample application')
app.mainloop()
