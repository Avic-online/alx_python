"""
this is a module of the program square that 
inherits from the rectangle
"""
from rectangle import Rectangle

class Square(Rectangle):
    """
    Here is the class square that inherits from the class rectangle
    as a parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """this is the default initialization method here as a constructor"""
        super().__init__(x, y, size, size, id)
    def __str__(self):
        """overides the string of the square"""
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'