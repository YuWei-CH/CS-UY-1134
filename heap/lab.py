from ArrayMinheap import ArrayMinHeap
from ChainingHashTableMap import ChainingHashTableMap
def min_merge_cost(ropes):
    cost = 0
    heap = ArrayMinHeap()
    for i in ropes:
        heap.insert(i)
    while (len(heap) > 1):
        first = heap.delete_min()
        second = heap.delete_min()
        total = first.priority + second.priority
        cost += total
        heap.insert(total)
    return cost

lst = [10, 5, 2, 14, 3, 8]
#print(min_merge_cost(lst))

def is_min_heap(lst):
    def is_min_heap_helper(lst,index):
        if index >= len(lst):
            return True

        check_left = True
        check_right = True

        if (index * 2 ) + 1 < len(lst):
            check_left = lst[index] < lst[index * 2 + 1]

        if index * 2 + 2 < len(lst):
            check_right = lst[index] < lst[index * 2 + 2]

        return check_left and check_right and is_min_heap_helper(lst,index*2+1) and is_min_heap_helper(lst,index*2+2)


    return is_min_heap_helper(lst,0)

#print(is_min_heap([4, 50, 7, 55, 90, 87]))


def k_most_frequent(lst, k):
    res = []
    heap = ArrayMinHeap()
    map = ChainingHashTableMap()
    for i in lst:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    for i in map:
        heap.insert(map[i],i)

    for i in range(len(map)- k):
        heap.delete_min()
    while heap.is_empty() is not True:
        res.append(heap.delete_min().value)
    return res

#print(k_most_frequent( [5,9,2,9,0,5,9,7], 3))

def merge_k_sorted_lsts(matrix):
    heap = ArrayMinHeap()
    result = []

    for i in range(len(matrix)):
        print(matrix[i][0])
        heap.insert(matrix[i][0],(i,0))

    while not heap.is_empty():
        item = heap.delete_min()
        min = item.priority
        position = item.value
        result.append(min)

        i,j = position
        if j + 1 < len(matrix[i]):
            heap.insert(matrix[i][j+1],(i,j+1))

    return result

matrix = [ [1, 47],
[-5,14,190],
[-1, 120],
[-3,1134] ]

print(merge_k_sorted_lsts(matrix))



