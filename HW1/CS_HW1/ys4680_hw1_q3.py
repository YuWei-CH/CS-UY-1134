# a
def sum_of_int_less_than_n(n):
    temp = 0
    while (n > 0):
        n -= 1
        temp += n**2
    return temp
# b
def sum_of_int_less_than_n(n):
   return sum(x**2 for x in range(n))
#c
def sum_of_odd_int_less_than_n(n):
    temp = 0
    while (n > 0):
        n -= 1
        if n % 2 != 0:
            temp += n**2
    return temp
#d
def sum_of_odd_int_less_than_n(n):
    return sum(x**2 for x in range(n) if x % 2 != 0)