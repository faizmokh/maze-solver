from time import sleep
from models.cell import Cell

class Maze:
    """
    Holds all the cells in the maze in 2D grid.
    A list of lists
    """
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self.cells = []
        
    def create_cells(self):
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                x1 = self.x1 + j * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                row.append(Cell(True, True, True, True, x1, y1, x2, y2, self.win))
            self.cells.append(row)
            
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if i == 0 and j == 0:
                    print(f"Start cell x={i}, y={j}")
                    self._draw_cell(i, j, has_top_wall=False)
                elif i == len(self.cells) - 1 and j == len(self.cells[i]) - 1:
                    print("End cell")
                    self._draw_cell(i, j, has_bottom_wall=False)
                else:
                    self._draw_cell(i, j)        

    def _draw_cell(self, i, j, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        x1, y1, x2, y2 = self._calculate_cell_location(i, j)
        cell = Cell(has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, y1, x2, y2, self.win)
        cell.draw()
        self._animate()
        
    def _animate(self):
        self.win.redraw()
        # sleep for 0.05 second
        sleep(0.05)
        
    def _calculate_cell_location(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        return x1, y1, x2, y2
            