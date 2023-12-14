"""
This program creates a class base geometry
and it raises the exception of this class!
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