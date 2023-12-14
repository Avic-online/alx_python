"""
Write a class Square that defines a
square by: (based on 2-square.py)
(python3 -c 'print(__import__("my_module").__doc__)')
"""

class Square:
    """
     (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    """
    def __init__(self, size=0):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'.
        """
        self.__size = size
        self.__validate_size()
    @property
    def size(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'.
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'.
        """
        self.__size = value
        self.__validate_size()

    def __validate_size(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'.
        """
        return self.__size ** 2