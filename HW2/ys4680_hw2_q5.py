def split_parity(lst):
    last_odd = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            lst[i], lst[last_odd] = lst[last_odd], lst[i]
            last_odd += 1
    return lst






