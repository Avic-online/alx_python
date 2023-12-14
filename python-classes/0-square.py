"""
Write a class Square that defines a square by:

Private instance attribute: size
Instantiation with size (no type/value verification)
You are not allowed to import any module
(python3 -c 'print(__import__("my_module").__doc__)')
"""

class Square:

    """
    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
     (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    """

    def __init__(self, size):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'.
        """
        self.__size = size