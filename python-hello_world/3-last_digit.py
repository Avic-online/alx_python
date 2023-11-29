#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
number_string = repr(number)
last_string_digit = number_string[-1]
lastDigit = int(last_string_digit)
if lastDigit > 5 :
    print('last digit of', str(number), 'is', str(lastDigit), 'and is greater than 5')
elif lastDigit == 0 :
    print('last digit of', str(number), 'is', str(lastDigit), 'and is zero')
elif lastDigit < 6 and lastDigit != 0 :
    print('last digit of', str(number), 'is', str(lastDigit), 'and is less than 6 and not 0')
else:
    pass