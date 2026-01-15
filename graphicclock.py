import tkinter
from tkinter import Tk, Canvas
import time

class GraphicClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphic Clock")
        self.canvas = Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        current_time = time.strftime("%H:%M:%S")
        self.canvas.create_text(200, 200, text=current_time, font=("Helvetica", 48), fill="black")
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = Tk()
    clock = GraphicClock(root)
    root.mainloop()