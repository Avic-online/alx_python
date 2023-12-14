#!/usr/bin/python3
Square = __import__('0-square').Square
# the square is now imported from the 0-square folder
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

# above is where the printing is done


try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)