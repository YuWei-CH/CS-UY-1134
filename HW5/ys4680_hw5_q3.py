from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque
class MidStack():
    def __init__(self):
        self.Stack = ArrayStack()
        self.Deque = ArrayDeque()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.Deque.enqueue_first(val)
        self.n += 1

    def top(self):
        if (self.is_empty()):
            raise Exception( "Stack is empty" )

        elif len(self)-1 == self.Stack.top()[1]:
            return self.Stack.top()[0]
        else:
            return self.Deque.first()

    def mid_push(self,val):
        if len(self) == 0:
            self.push(val)
        elif len(self)%2 == 0:
            self.Stack.push([val,len(self)/2])
        else:
            self.Stack.push([val,(len(self)//2) +1])
        self.n += 1

    def pop(self):
        if (self.is_empty()):
            raise Exception( "Stack is empty" )

        elif self.Stack.is_empty():
            self.n -= 1
            return self.Deque.dequeue_first()

        elif len(self)-1 == self.Stack.top()[1]:
            self.n -= 1
            temp = self.Stack.pop()[0]
            return temp

        else:
            self.n -= 1
            return self.Deque.dequeue_first()


'''
temp = MidStack()
temp.mid_push(1)
temp.push(2)
temp.push(4)
temp.push(6)
temp.push(8)
temp.push(10)
temp.mid_push(12)
print(temp.top())
print(temp.pop())
print(temp.top())
print(temp.pop())
print(temp.top())
print(temp.pop())
print(temp.top())
print(temp.pop())
print(temp.pop())
print(temp.pop())
print(temp.pop())
print(temp.pop())
print(temp.pop())
print(temp.pop())
print(temp.pop())

'''