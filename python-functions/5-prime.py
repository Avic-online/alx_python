def is_prime(number):
    prime1 = 6 * number - 1
    prime2 = 6 * number + 1
    if number == prime1 or number == prime2 :
        return True
    else:
        return False
#   or number==2 or number==3   
print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))