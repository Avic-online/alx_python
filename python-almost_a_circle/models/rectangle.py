"""
this is a documentation of the module
here we will import the Base class from our python base file
and do some inheritance
"""
from models.base import Base

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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
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
        # for _ in range(self.width):
        #     print('#' * self.width)
        for _ in range(self.y):
            print()  # Print empty lines for y

        for _ in range(self.height):
            print('#' * self.width)
            # print(' ' * self.x  + '#' * self.width)

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
        self.validate_integer(value, 'width')
        self.validate_positive(value, 'width')
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
        self.validate_integer(value, 'height')
        self.validate_positive(value, 'height')
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
        self.validate_integer(value, 'x')
        self.validate_non_negative(value, 'x')
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
        self.validate_integer(value, 'y')
        self.validate_non_negative(value, 'y')
        self.__y = value

    def validate_integer(self, value, height):
        """Validates that the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{height} must be an integer")

    def validate_positive(self, value, width):
        """Validates that the value is greater than 0."""
        if value <= 0:
            raise ValueError(f"{width} must be > 0")

    def validate_non_negative(self, value, x):
        """Validates that the value is greater than or equal to 0."""
        if value < 0:
            raise ValueError(f"{x} must be >= 0")
    def validate_non_negative(self, value, y):
        """Validates that the value is greater than or equal to 0."""
        if value < 0:
            raise ValueError(f"{y} must be >= 0")
   