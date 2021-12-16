from ChainingHashTableMap import ChainingHashTableMap

def most_frequent(lst):
    map = ChainingHashTableMap()
    for i in lst:
        if i not in map:
            map[i] = 0
        else:
            map[i] += 1
    max_num = 0
    max_index = None
    for i in map:
        if map[i] > max_num:
            map[i] = max_num
            max_index = i
    return max_index

#print(most_frequent([5,9,2,9,0,5,9,7]))
def first_unique(lst):
    map = ChainingHashTableMap()
    for i in lst:
        if i not in map:
            map[i] = 0
        else:
            map[i] += 1
    for i in lst:
        if map[i] == 0:
            return i
    return None

#print(first_unique([5,9,2,9,0,5,9,7]))

def two_sum(lst,target):
    map = ChainingHashTableMap()
    for i in range(len(lst)):
        try:
            if map[target-lst[i]]:
                return (map[target-lst[i]],i)
        except:
            map[lst[i]] = i


    return (None,None)

print(two_sum( [-2, 11, 15, 21, 20, 7],22))