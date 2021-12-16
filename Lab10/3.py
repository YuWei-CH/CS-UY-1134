from DoublyLinkedList import DoublyLinkedList
class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.mid = self.data.header

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self.data) == 0)

    def push(self, e):
        self.data.add_first(e)
        if len(self) ==1:
            self.mid = self.data.header.next
        elif len(self) % 2 !=0:
            self.mid = self.mid.next

    def top(self):
        return self.data.header.next.data

    def pop(self):
        val = self.data.delete_first()
        if self.is_empty():
            self.mid = None
        elif len(self) % 2 == 0:
            self.mid = self.mid.prev
        return val

    def mid_push(self,e):
        self.data.add_before( self.mid, e )
        if len( self ) == 1:
            self.mid = self.data.header.next
        elif len( self ) % 2 != 0:
            self.mid = self.mid.next

    def get_mid(self):
        return self.mid.data

'''
1
'''



m =MidStack()
m.push(1)
m.push(3)
m.mid_push(2)



print(m.pop())
print(m.pop())
print(m.pop())