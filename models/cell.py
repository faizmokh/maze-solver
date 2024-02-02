from models.line import Line
from models.point import Point

class Cell:
    """
    holds data about individual cell
    """
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, y1, x2, y2, win):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.win = win
        
    def draw(self, fill_color="black"):
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), fill_color)
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), fill_color)
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), fill_color)
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), fill_color)
        
    def draw_move(self, to_cell, undo=False):
        line_color = "gray" if undo else "red"
        
        is_adjacent = self.is_adjacent(to_cell)
        print(is_adjacent)
        mid_point = self.mid_point()
        to_mid_point = to_cell.mid_point()
        print("GOES HERE")
        self.win.draw_line(Line(mid_point, to_mid_point), line_color)
        
        
    def mid_point(self):
        return Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
    
    def is_adjacent(self, other_cell):
        return (abs(self.x1 - other_cell.x1) == 1 and self.y1 == other_cell.y1) or (self.x2 == other_cell.x2 and abs(self.y2 - other_cell.y2) == 1)