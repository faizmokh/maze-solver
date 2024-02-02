import tkinter as tk

from models.line import Line

class Window:
    
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.running = False
    
    def loop(self):
        self.root.mainloop()
        
    def redraw(self, window):
        window.update()
        window.update_idletasks()
        
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw(self.root)
            
    def close(self):
        self.running = False
        self.root.destroy()
        
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.canvas, fill_color)