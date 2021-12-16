from ChainingHashTableMap import ChainingHashTableMap

def two_sum(lst, target):
    hashtable = ChainingHashTableMap()
    index = 0
    for i in lst:
        hashtable.__setitem__(22-i,i)
        index += 1

    temp = None
    for j in lst:
        if j in hashtable and j is not hashtable[j]:
            temp = (j,hashtable[j])

    index = 0
    if temp is not None:
        for m in range(len(lst)):
            if temp[0] is lst[m]:
                first = m
            elif temp[1] is lst[m]:
                second = m
        return (first,second)
    else:
        return (None, None)

lst = [-2, 11, 15, 21, 20, 17]
print(two_sum(lst, 22))




