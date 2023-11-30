# here we define the function
def convert_to_celsius(fahrenheit):
    # fahrenheit = int(input("Enter temperature in degree celsius:"))
    celcius = (5/9)*(fahrenheit - 32)
    return celcius
# here we call the function
print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))