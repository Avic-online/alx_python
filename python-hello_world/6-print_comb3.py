for numbers in range(90):
    if int(repr(numbers)[0]) != int(repr(numbers)[-1]):
        print('{:02}'.format(numbers), end=", ")