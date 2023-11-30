def is_prime(number):
    i = 0
    # for positive number input
    if number > 1:
# for the range of the prime number
        for i in range(2,number):
            if (number % i) == 0:
                return False
            else:
                pass
        else:
            return True
    else:
        return False