import math
import tkinter as tk
from tkinter import Tk, Canvas

class GraphicCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Graphic Calculator")
        self.canvas = Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.display_text = "0"
        self.button_areas = []  
        self.draw_calculator()

    def draw_calculator(self):
        self.canvas.delete("all")
        self.button_areas.clear()
        self.canvas.create_rectangle(50, 50, 350, 350, fill="lightgrey", outline="black")
        self.canvas.create_rectangle(70, 70, 330, 120, fill="white", outline="black")
        
        self.canvas.create_text(200, 95, text=self.display_text, font=("Helvetica", 24), fill="black", tags="display")

        button_labels = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        x_start = 70
        y_start = 140
        button_width = 60  
        button_height = 40
        padding = 10

        for i, label in enumerate(button_labels):
            x = x_start + (i % 4) * (button_width + padding)
            y = y_start + (i // 4) * (button_height + padding)
            rect = self.canvas.create_rectangle(x, y, x + button_width, y + button_height, fill="white", outline="black", tags=(f"btn_{label}", "button"))
            self.canvas.create_text(x + button_width / 2, y + button_height / 2, text=label, font=("Helvetica", 18), fill="black", tags=(f"btn_{label}",))
            
            self.button_areas.append((x, y, x + button_width, y + button_height, label))

        self.canvas.tag_bind("button", "<Button-1>", self.on_canvas_click)

    def on_canvas_click(self, event):
        
        for x1, y1, x2, y2, label in self.button_areas:
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                self.handle_button(label)
                break

    def handle_button(self, label):
        if label in '0123456789.':
            if self.display_text == "0":
                self.display_text = label
            else:
                self.display_text += label
        elif label in '+-*/':
            if self.display_text[-1] in '+-*/':
                self.display_text = self.display_text[:-1] + label
            else:
                self.display_text += label
        elif label == '=':
            try:
                
                result = str(eval(self.display_text))
                self.display_text = result
            except Exception:
                self.display_text = "Error"
        self.draw_calculator()

if __name__ == "__main__":
    root = Tk()
    calculator = GraphicCalculator(root)
    root.mainloop()