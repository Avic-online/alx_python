"""
This is the program for class inheritance
it over-writes and also displays square
"""
class BaseGeometry:
    """ This is the class for Base Geometry"""
    def __init__(self):
        """ This function is for initialization """ 
        pass 
    def area(self):
        """ This method is for the area of the base geometry with
            an exception
        """    
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ This is the integer validator of the method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
    
class Rectangle(BaseGeometry):
    """ This is the inherited class of the base geometry"""
    def __init__(self, width, height):
        """ This is the over-writing method of the base geometry"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def area(self):
        """ This is the area over-write of base geometry"""
        return self.__width * self.__height
    def __str__(self):
        """ This is the string method"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    
class Square(Rectangle):
    """ This class is inherited from the super/parent class rectangle"""
    def __init__(self, size):
        """ This method over-writes the method for the rectangle initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size