from ArrayMinheap import ArrayMinHeap
from ChainingHashTableMap import ChainingHashTableMap
'''
[10, 5, 2, 14, 3, 8]
[2,3,5,8,10,14] 0
[5,5,8,10,14] 5
[10,8,10,14] 15
[18,10,14] 33
[24,18] 57
[42] 99
'''

def min_merge_cost(ropes):
    heap = ArrayMinHeap()
    cost = 0
    for i in ropes:
        heap.insert(i)
    while  len(heap) > 1:
        first = heap.delete_min().priority
        second = heap.delete_min().priority
        total = first + second
        cost += total
        heap.insert(total)
    return cost

#print(min_merge_cost([10, 5, 2, 14, 3, 8]))

def is_min_heap(lst):
    def is_min_heap_helper(lst,index):
        left = True
        right = True
        if index > len(lst)-1:
            return True
        else:
            if index * 2+1 < len(lst):
                left = lst[index] < lst[index * 2+1]
            if index * 2+2 < len(lst):
                right = lst[index] < lst[index * 2+2]
            return left and right and is_min_heap_helper(lst,index * 2+1) and is_min_heap_helper(lst,index * 2+2)
    return is_min_heap_helper(lst,0)
#print(is_min_heap([4, 50, 7, 55, 90, 87]))
#print(is_min_heap([10, 50, 7, 55, 90, 87]))

def k_most_frequent(lst, k):
    map = ChainingHashTableMap()
    heap = ArrayMinHeap()
    res= []
    for i in lst:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    for i in map:
        heap.insert(map[i],i)

    for i in range(len(map) - k):
        heap.delete_min()

    while not heap.is_empty():
        res.append(heap.delete_min().value)

    return res

#print(k_most_frequent([5,9,2,9,0,5,9,7],2))


def merge_k_sorted_lsts(matrix):
    heap = ArrayMinHeap()
    lst = []
    for i in range(len(matrix)):
        heap.insert(matrix[i][0],(i,0))
    while not heap.is_empty():
        min = heap.delete_min()
        lst.append(min.priority)
        position = min.value
        i,j = position
        if j + 1 < len(matrix[i]):
            j = j + 1
            heap.insert(matrix[i][j],(i,j))
    return lst
matrix = [ [1, 5, 47],
[-5, 2, 3, 10, 12],
[45, 100, 120],
[-3, 0, 0, 1, 120, 1134] ]
print(merge_k_sorted_lsts(matrix))





