def all_fibonacci_numbers():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
