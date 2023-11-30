#!/usr/bin/env python3
# here we import the function for convert to celsius

convert_to_celsius = __import__('2-temperature').convert_to_celsius

# here is the output

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))