from models.point import Point

class Line:
    """
    A class to represent a line in 2D space.
    """
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        
    def __repr__(self):
        return f"Line({self.start}, {self.end})"
    
    def __str__(self):
        return f"Line from {self.start} to {self.end}"
    
    def draw(self, canvas, color="black"):
        canvas.create_line(self.start.x, self.start.y, self.end.x, self.end.y, fill=color, width=2)
        canvas.pack()