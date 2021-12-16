from DoublyLinkedList import DoublyLinkedList

class LinkedQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self.data) == 0)

    def enqueue(self, elem):
        self.data.add_first(elem)

    def dequeue(self):
        return self.data.delete_last()

    def first(self):
        return self.data.trailer.prev.data


'''
s = LinkedQueue()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)

print(s.is_empty()) # false
print(s.dequeue()) # 1
print(s.first()) # 2
print(s.dequeue()) # 2
print(s.dequeue()) # 3
'''