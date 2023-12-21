"""
this is a documentation of the module
here we will import the Base class from our python base file
and do some inheritance
"""
from base import Base

"""
imported module above
okay
"""

class Rectangle(Base):
    """
    This is a class Rectangle that inherits from another class,
    now its super class, Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.
        this function initializes itself with arguments
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """
        super class for the id
        """
    def area(self):
        """
        this is the area method in the class
        """
        return self.height * self.width
    
    def display(self):
        """This diaplays an output with #"""
        for _ in range(self.width):
            print('#' * self.width)
        for _ in range(self.y):
            print()  # Print empty lines for y

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Override the string of our rectangle."""
        return f'[Rectangle] ({id(self)}) {self.x}/{self.y} - {self.width}/{self.height}'

    @property
    def width(self):
        """
        this is to get the variable width
        """
        return self.__width
        
    
    @width.setter
    def width(self, value):
        """
        this is to set the variable width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        """
        this is to get height
         """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        this is to set y
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    @property
    def x(self):
        """
        this is to set y
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        this is to set y
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        this is to set y
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        this is to set y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        self.__y = value