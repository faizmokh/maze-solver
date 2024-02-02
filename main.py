import tkinter as tk

from line import Line
from point import Point

window_width = 500
window_height = 500

class Window:
    
    def __init__(self, width=window_width, height=window_height):
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

def main():
    window = Window(800, 600)
    
    window.draw_line(Line(Point(100, 100), Point(200, 100)))
    window.draw_line(Line(Point(200, 100), Point(200, 200)))
    
    window.wait_for_close()
    
if __name__ == "__main__":
    main()