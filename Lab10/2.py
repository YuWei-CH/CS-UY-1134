class DoublyLinkedList_Pro:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList_Pro.Node()
        self.trailer = DoublyLinkedList_Pro.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len( self ) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList_Pro.Node( val )
        prev_node = node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        next_node.prev = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after( self.header, val )

    def add_last(self, val):
        return self.add_after( self.trailer.prev, val )

    def add_before(self, node, val):
        return self.add_after( node.prev, val )

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if (self.is_empty() == True):
            raise Exception( "List is empty" )
        return self.delete_node( self.header.next )

    def delete_last(self):
        if (self.is_empty() == True):
            raise Exception( "List is empty" )
        return self.delete_node( self.trailer.prev )

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __getitem__(self, i):
        if i > len(self)//2:
            n = len(self)-1
            cursor = self.trailer.prev
            while n > i:
                n -= 1
                cursor = cursor.prev
            return cursor.data
        else:
            n = 0
            cursor = self.header.next
            while n < i:
                n +=1
                cursor = cursor.next
            return cursor.data

    def __repr__(self):
        return "[" + " <--> ".join( [str( elem ) for elem in self] ) + "]"


s = DoublyLinkedList_Pro()
s.add_last(1)
s.add_last(2)
s.add_last(3)
print(s[0])
