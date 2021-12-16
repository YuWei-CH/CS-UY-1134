def factors(num):
    standard = num**0.5
    lst = []
    for i in range(1,int(standard)+1):
        if num % i == 0:
            yield i
            lst.append(i)
    if num**0.5 == int(standard):
        lst.pop()
    while i < num:
        i = int(num / lst.pop())
        yield i