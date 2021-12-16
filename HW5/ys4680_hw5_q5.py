from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue
import copy
def permutations(lst):
    queue = ArrayQueue()
    stack = ArrayStack()
    result = []
    for i in lst:
        stack.push(i)
    queue.enqueue([])

    for j in range(len(stack)):
        temp = stack.pop()
        for m in  range(len(queue)):
            for n in range (j+1):
                print( m )
                new_temp = queue.first()
                queue.enqueue(new_temp[:n]+[temp]+new_temp[n:])
            a = queue.dequeue()

    for s in range(len(queue)):
        result.append(queue.dequeue())

    return result


lst = [1,2,3]
print(permutations(lst))


"""
def permutations(lst):
    queue = ArrayQueue()
    stack = ArrayStack()
    result = []
    for i in lst:
        queue.enqueue(i)
    for q in range(len(lst)+1):
        for i in range(len(lst)):
            temp_result = []
            temp_result.append(lst[i])
            for j in range(len(queue)):
                temp = queue.dequeue()
                if temp != lst[i]:
                    temp_result.append(temp)
                    stack.push(temp)
                #print(temp_result,'temp_result')
            if temp_result not in result:
                result.append( temp_result )
            temp_result = []
            temp_result.append(lst[i])
            queue.enqueue(lst[i])
            for n in range(len(stack)):
                temp = stack.pop()
                temp_result.append(temp)
                queue.enqueue( temp )
            if temp_result not in result:
                result.append(temp_result)
            temp_result = []
    return result
"""