def fun3(n):
    if (n == 0):
        return 1
    else:
        res = fun3(n//2)
        print(n,'n')
        for i in range(1, n+1):
            print(i)
            res += i
        return res


print(fun3(8))