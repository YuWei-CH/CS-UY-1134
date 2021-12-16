from ChainingHashTableMap import ChainingHashTableMap
def intersection_list(lst1, lst2):
    hashmap = ChainingHashTableMap()
    res = []
    for i in lst1:
        hashmap[i] = '*'

    for i in lst2:
        try:
            nothing = hashmap[i]
            res.append(i)
        except KeyError:
            pass
    return res

'''
lst1 = [3, 9, 2, 7, 1]
lst2 = [4, 1, 8, 2]

print(intersection_list1(lst1,lst2))
print(intersection_list2(lst1,lst2))
'''