import random
from time import sleep
from models.cell import Cell

class Maze:
    """
    Holds all the cells in the maze in 2D grid.
    A list of lists
    """
    
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.seed = seed if seed is not None else random.seed(seed)
        self.cells = []
        
    def start(self):
        self.create_cells()
        self.break_walls_r(0, 0)
        self.reset_cells_visited()
        self.solve()
        
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

    def _draw_cell(self, i, j, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        x1, y1, x2, y2 = self._calculate_cell_location(i, j)
        cell = Cell(has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, y1, x2, y2, self.win)
        cell.draw()
        self._animate()
        
    def _animate(self):
        self.win.redraw()
        # sleep for 0.01 second
        sleep(0.01)
        
    def _calculate_cell_location(self, i, j):
        x1 = self.x1 + j * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        return x1, y1, x2, y2
            
    def break_walls_r(self, i, j):
        print(f"Breaking walls for cell x={i}, y={j}")
        self.cells[i][j].visited = True
        
        while True:
            neighbors = []
            
            for (neighbor_i, neighbor_j) in self.get_valid_neighbors(i, j):
                if not self.cells[neighbor_i][neighbor_j].visited:
                    neighbors.append((neighbor_i, neighbor_j))
                    
            if not neighbors:
                if i == 0 and j == 0:
                    self.cells[i][j].has_top_wall = False
                elif i == self.num_rows - 1 and j == self.num_cols - 1:
                    self.cells[i][j].has_bottom_wall = False
                self._draw_cell(
                    i, 
                    j, 
                    has_left_wall=self.cells[i][j].has_left_wall, 
                    has_right_wall=self.cells[i][j].has_right_wall, 
                    has_top_wall=self.cells[i][j].has_top_wall, 
                    has_bottom_wall=self.cells[i][j].has_bottom_wall
                    )
                return
            
            neighbor_index = random.randrange(len(neighbors))
            ni, nj = neighbors[neighbor_index]
            
            self.remove_wall(i, j, ni, nj)

            self.break_walls_r(ni, nj)
            
    def get_valid_neighbors(self, i, j):
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if i < self.num_rows - 1:
            neighbors.append((i + 1, j))
        if j < self.num_cols - 1:
            neighbors.append((i, j + 1))
        return neighbors

    def remove_wall(self, i, j, ni, nj):
        if i == ni and j > nj:
            self.cells[i][j].has_left_wall = False
            self.cells[ni][nj].has_right_wall = False
        elif i == ni and j < nj:
            self.cells[i][j].has_right_wall = False
            self.cells[ni][nj].has_left_wall = False
        elif j == nj and i > ni:
            self.cells[i][j].has_top_wall = False
            self.cells[ni][nj].has_bottom_wall = False
        elif j == nj and i < ni:
            self.cells[i][j].has_bottom_wall = False
            self.cells[ni][nj].has_top_wall = False
        else:
            raise ValueError("Invalid wall removal")
        
    def reset_cells_visited(self):
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.cells[i][j].visited = False
                
    def solve(self):
        print("Solving maze...")
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        current_cell = self.cells[i][j]
        if i == self.num_rows - 1 and j == self.num_cols - 1:
            return True
        
        if (j + 1 < self.num_cols 
            and self.cells[i][j + 1] != None 
            and not self.cells[i][j + 1].visited 
            and not self.cells[i][j].has_right_wall):
            current_cell.draw_move(self.cells[i][j + 1])
            self.cells[i][j + 1].visited = True
            if self._solve_r(i, j + 1):
                return True
            else:
                self.cells[i][j + 1].visited = True
                current_cell.draw_move(self.cells[i][j + 1], undo=True)
                
        if (i + 1 < self.num_rows 
              and self.cells[i + 1][j] != None 
              and not self.cells[i + 1][j].visited 
              and not self.cells[i][j].has_bottom_wall):
            current_cell.draw_move(self.cells[i + 1][j])
            self.cells[i + 1][j].visited = True
            if self._solve_r(i + 1, j):
                return True
            else:
                self.cells[i + 1][j].visited = True
                current_cell.draw_move(self.cells[i + 1][j], undo=True)
        
        if(j - 1 < self.num_cols 
             and self.cells[i][j - 1] != None 
             and not self.cells[i][j - 1].visited 
             and not self.cells[i][j - 1].has_right_wall):
            current_cell.draw_move(self.cells[i][j - 1])
            self.cells[i][j - 1].visited = True
            if self._solve_r(i, j - 1):
                return True
            else:
                self.cells[i][j - 1].visited = True
                current_cell.draw_move(self.cells[i][j - 1], undo=True)
        if (i - 1 < self.num_rows
              and self.cells[i - 1][j] != None 
              and not self.cells[i - 1][j].visited 
              and not self.cells[i - 1][j].has_bottom_wall):
            current_cell.draw_move(self.cells[i - 1][j])
            self.cells[i - 1][j].visited = True
            if self._solve_r(i - 1, j):
                return True
            else:
                self.cells[i - 1][j].visited = True
                current_cell.draw_move(self.cells[i - 1][j], undo=True)
        
        return False
    
