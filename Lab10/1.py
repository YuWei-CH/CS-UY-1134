from DoublyLinkedList import DoublyLinkedList

class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (self.n == 0)

    def push(self, e):
        self.n += 1
        self.data.add_first(e)

    def pop(self):
        self.n -= 1
        res = self.data.delete_first()
        return res

    def top(self):
            return self.data.header.next.data


s = LinkedStack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.top())