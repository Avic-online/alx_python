"""
Write a class Square that
defines a square by: (based on 3-square.py)
"""

class Square:
    """
    okay okay okay
    """
    def __init__(self, size=0):
        """
        function okay okay okay
        """
        self.__size = size
        self.__validate_size()
    @property
    def size(self):
        """
        property getter here
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        set the size of the new square here
        """
        self.__size = value
        self.__validate_size()

    def __validate_size(self):
        """
        place where size is validated
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """
        this is doc for the area
        """
        return self.__size ** 2
    
    def my_print(self):
        """
        Prints the square using the character '#' in stdout.
        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)