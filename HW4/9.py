def permutations(lst, low, high):
    if low == high:
        return lst
    result = []
    j = low
    for i in range(low, high):  # 从begin到end全排列。
        lst[i], lst[j] = lst[j], lst[i]
        result.apend(permutations(lst, low + 1, high))
        lst[i], lst[j] = lst[j], lst[i]  # 递归完成后，交换回原来的位置。
    return result

arr = [1, 2, 3]
print(permutations(arr, 0, len(arr)))
'''
def permut1(array):
    if len(array) == 1:
        return [array]
    res = []
    for permutation in permut1(array[1:]):
        print(array,'bbb')
        print(permutation)
        for i in range(len(array)):
            print(i)
            res.append(permutation[:i] + array[0:1] + permutation[i:])
    return res



lst = [1,2,3]
print(permut1(lst))
print('112345')
'''