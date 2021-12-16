"""
4.a: the worst-case running	time of the implementation above is ϴ(n^2)
"""


def remove_all(list, val):
    counter = 0
    for i in range(len(list)):
        if list[i] != val:
            list[counter], list[i] = list[i],list[counter]
            counter += 1
    for j in range(len(list)-counter):
        list.pop()
    return list
"""
4.c : the worst-case running time of the implementation above is ϴ(n)
"""