import tkinter as tk
from models.cell import Cell
from models.maze import Maze

from models.window import Window
from models.line import Line
from models.point import Point

def main():
    window = Window(800, 600)
    # calculate number of rows and columns based on cell size and window size
    cell_size = 50
    
    print(f"{window.canvas.winfo_height()} x {window.canvas.winfo_width()}")
    
    num_rows = window.canvas.winfo_height() // cell_size
    num_cols = window.canvas.winfo_width() // cell_size
        
    maze = Maze(0, 0, num_rows, num_cols, cell_size, cell_size, window)
    maze.create_cells()
    
    window.wait_for_close()
    
if __name__ == "__main__":
    main()