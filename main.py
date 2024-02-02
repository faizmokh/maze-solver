from calendar import c
import tkinter as tk
from models.cell import Cell

from window import Window
from models.line import Line
from models.point import Point

def main():
    window = Window(800, 600)
    
    # draw 2 adjacent cells
    cell1 = Cell(True, False, True, True, 100, 100, 200, 200, window)
    cell2 = Cell(False, True, True, True, 200, 100, 300, 200, window)
    cell1.draw()
    cell2.draw()
    
    # draw a move from cell1 to cell2
    cell1.draw_move(cell2)
    
    window.wait_for_close()
    
if __name__ == "__main__":
    main()