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
"""
here is where the class starts 
the class inheits from base class
so base class is now its super class
"""
class Rectangle(Base):
    """
    This is a class Rectangle that inherits from another class,
    now its super class, Base
    """

     """the property call is a getter function for the
    width of our rectangle"""
    @property
    def width(self):
        """
        this is to get the variable width
        it has an @property function
        this get will come with a setter
        """
        return self.__width  #this returns private width variable
        
    """the setter call is a
    setter function for the width of our rectangle"""
    @width.setter
    def width(self, value):
        """
        this is to set the variable width
        it has an @arg.setter function
        this setter had a getter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    """the property call is a
    getter function for the height of our rectangle"""
    @property
    def height(self):
        """
        this is to get height with a variable arg self 
        which is a self assigned argument for the method
         """   
        return self.__height    #this returns private height variable
    

    """the setter call is a
    setter function for the height of our rectangle"""
    @height.setter
    def height(self, value):
        """
        this is to set height of with a self arg and a value
        argument declared on it
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """the getter call is a
    getter function for x of our rectangle"""
    @property
    def x(self):
        """
        this is to set x of with a self arg and a value
        argument declared on it
        """
        return self.__x    #this returns private x variable
    
    """the setter call is a
    setter function for x of our rectangle"""
    @x.setter
    def x(self, value):
        """
        this is to set height of with a self arg and a value
        argument declared on it
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """the getter call is a
    getter function for y of our rectangle"""
    @property
    def y(self):
        """
        this is to set height of with a self arg and a value
        argument declared on it
        """
        return self.__y     #this returns private y variable
    
    """the setter call is a
    setter function for y of our rectangle"""
    @y.setter
    def y(self, value):
        """
        this is to set height of with a self arg and a value
        argument declared on it
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.
        this function initializes itself with arguments
        """
        super().__init__(id)

        """
        this is a documentation of the module
        here we will import the Base class from our python base file
        and do some inheritance
        """

        self._width = width
        self._height = height
        self._x = x
        self._y = y
        """
        super class for the id
        also declaration of the variables assignment
        """
    """under is the method for area with a self arg"""
    def area(self):
        """
        this is the area method in the class
        it has a self arg
        """
        return self.height * self.width   #this will return an area
        
    """below starts the method for display method with a self arg"""
    def display(self):
        """
        This diaplays an output with #
        it has a for loop statement
        """
        for _ in range(self.width):
            print('#' * self.width)
        for _ in range(self.y):
            print()  # Print empty lines for y

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    """this is the string method/function starting below"""
    def __str__(self):
        """Override the string of our rectangle."""
        return f'[Rectangle] ({id(self)}) {self.x}/{self.y} - {self.width}/{self.height}'
    
    """The function below updates our rectangle"""
    def update(self, *args, **kwargs):
        """this class method updates the rectangle attribute"""
        if args:
            #use this condition to update the table if args is not empty
            if len(args) >= 1:
                self.x = args[0]
            elif len(args) >= 2:
                self.width = args[1]
            elif len(args) >= 3:
                self.height = args[2]
            elif len(args) >= 4:
                self.x = args[3]
            elif len(args) >= 5:
                self.y =args[4]
        elif kwargs:
            # use this condition of keyword argument to update rectangle
            # if the args is empty
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)

   