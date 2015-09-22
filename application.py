import Tkinter as tk
import time
from threading import Thread

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.canvas = tk.Canvas(self, height = 200, width = 400)
        self.canvas.grid(column = 0)
        self.quitButton = tk.Button(self, text='Quit',command=self.quit)
        self.quitButton.grid(column = 1)

        t = Thread(target=self.move_rect)
        t.start()

    def move_rect(self):

        rect = self.canvas.create_rectangle(150, 20, 200, 70)

        for i in xrange(1, 100):
            x0, y0, x1, y1 = self.canvas.coords(rect)
            self.canvas.move(rect, -1, 0)
            self.canvas.update()
            time.sleep(0.025)

        self.quit()

app = Application()
app.master.title('Sample application')
app.mainloop()
