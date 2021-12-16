def e_approx(n):
    result = 1
    record = 1
    for i in range(1,n+1):
        result += 1 / (record * i)
        record = record * i
    return result