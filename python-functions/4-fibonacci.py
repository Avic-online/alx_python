# fibonnacci sequence

def fibonacci_sequence(n):
    if n <= 0:
        return []

    fibonacci_numbers = []
    a, b = 0, 1

    while len(fibonacci_numbers) < n:
        fibonacci_numbers.append(a)
        a, b = b, a + b

    return fibonacci_numbers
