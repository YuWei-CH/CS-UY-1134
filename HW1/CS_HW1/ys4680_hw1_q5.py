def fibs(n):
    a, b = 0, 1
    while n > 0:
        yield b
        a, b = b, b + a
        n -= 1