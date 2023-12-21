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

    @property
    def width(self):
        return self.__width
        """
        this is to get the variable width
        """
    
    @width.setter
    def width(self, value):
        self.__width = value
        """
        this is to set the variable width
        """
    @property
    def height(self):
        return self.__height
        """
        this is to get height
         """
    
    @height.setter
    def height(self, value):
        self.__height = value
        """
        this is to set y
        """
    @property
    def x(self):
        return self.__x
        """
        this is to set y
        """
    
    @x.setter
    def x(self, value):
        self.__x = value
        """
        this is to set y
        """

    @property
    def y(self):
        return self.__y
        """
        this is to set y
        """
    
    @y.setter
    def y(self, value):
        self.__y = value
        """
        this is to set y
        """