from ArrayQueue import ArrayQueue
class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
        self.sum = 0

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data)

    def enqueue(self,e):
        if not isinstance(e,int) or not isinstance(e,float):
            self.data.enqueue(e)
            self.sum += e

    def dequeue(self):
        return self.data.dequeue()

    def first(self):
        return self.data.first()

    def sum(self):
        return self.sum

    def mean(self):
        return self.sum / len(self)


class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        self.data.enqueue(e)

    def pop(self):
        pass


    def top(self):
        pass

# lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
def flatten_list_by_depth(lst):
    q = ArrayQueue()
    new_lst = []
    for i in lst:
        q.enqueue(i)

    while len(q) > 0:
        for i in range(len(q)):
            temp = q.dequeue()
            if isinstance(temp,int):
                new_lst.append(temp)
            elif isinstance(temp,list):
                for j in temp:
                    q.enqueue(j)
    return  new_lst


'''
lst = [ [[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
new_lst = flatten_list_by_depth(lst)
print(new_lst) # [3, 9, 1, 2, 4, 8, 5, 6, 0, 7]
'''

def genBinary(n):
    q = ArrayQueue()
    q.enqueue('1')
    lst = []
    while n > 0:
        n -= 1
        temp = q.dequeue()
        lst.append(temp)

        q.enqueue(temp+'0')
        q.enqueue(temp+'1')
    return lst

print(genBinary(10))
