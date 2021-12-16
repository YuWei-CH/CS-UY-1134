from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack


def mystery(s):
    if len(s) == 1:
        return s.top()
    else:
        val = s.pop()
        result = mystery(s)
        if val < result:
            result = val
        s.push(val)
        return result

s = ArrayStack()
s.push(4)
s.push(3)
s.push(2)
s.push(4)
print(mystery(s))


def mystery(q):
    if (q.is_empty()):
        return
    else:
        val = q.dequeue()
        mystery(q)
        if val % 2 != 0:
            q.enqueue(val)



q = ArrayQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(4)
q.enqueue(8)
mystery(q)
print(len(q))
print(q.data)



def mystery(input_str):
    s = ArrayStack()
    q = ArrayQueue()
    for char in input_str:
        s.push(char)
        q.enqueue(char)
    while not s.is_empty():
        if s.pop() != q.dequeue():
            return False
    return True

print(mystery('aabba1'))