import random
from UnsortedArrayMap import UnsortedArrayMap
#from DoublyLinkedList import DoublyLinkedList

class DoublyLinkedList:
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
        self.header = DoublyLinkedList.Node()  # a node with Note prev, None data, None next
        self.trailer = DoublyLinkedList.Node()  #
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len( self ) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node( val )
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
        return self.add_after( self.trailer.prev, val )  # 保证一直在trailer前

    def add_before(self, node, val):
        return self.add_after( node.prev, val )  # node前面

    def delete_node(self, node):  # 绕过了这个node
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
        return self.delete_node( self.header.next )  # 直接把header和后面node的连接起来

    def delete_last(self):
        if (self.is_empty() == True):
            raise Exception( "List is empty" )
        return self.delete_node( self.trailer.prev )  # 把node和trailer链接了

    def __iter__(self):
        cursor = self.header.next
        while (cursor is not self.trailer):  # 循环untill trailer
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join( [str( elem ) for elem in self] ) + "]"


import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()


class ChainingHashTableMap:

    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N



    def __init__(self, N=64):
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = UnsortedArrayMap()
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)
        self.iter_list = DoublyLinkedList()
        self.nodeholder = None


    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.h(key) #返回一个index
        curr_bucket = self.table[i]
        #print(key)
        return curr_bucket[key][0]

    def __setitem__(self, key, value):
        i = self.h(key)
        curr_bucket = self.table[i]
        old_size = len( curr_bucket )
        if len(self.iter_list) == 0:
            self.iter_list.add_last(key)
            self.nodeholder = self.iter_list.trailer.prev
            curr_bucket[key] = (value,self.nodeholder)
        else:
            is_key_here = False
            if key in self.iter_list:
                is_key_here = True
                curr_bucket[key] = (value,curr_bucket[key][1])
            if is_key_here == False:
                self.iter_list.add_last(key)
                self.nodeholder = self.iter_list.trailer.prev
                curr_bucket[key] = (value, self.nodeholder)
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1 #判断在UnsortedArrayMap里面是mutate了还是append了
        if (self.n > len(self.table)):
            self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        self.iter_list.delete_node(curr_bucket[key][1])
        del curr_bucket[key]
        self.n -= 1
        if (self.n < len(self.table) // 4):
            self.rehash(len(self.table) // 2)

    def __contains__(self, key):
        try:
            val = self[key] #调用了 __getitem__ method
            return True
        except KeyError:
            return False

    def __iter__(self):
        for i in self.iter_list:
                yield i

    def rehash(self, new_size):
        #print('re')
        old = [(key, self[key]) for key in self]
        self.__init__( new_size )
        for (key, val) in old:
            self[key] = val

a = ChainingHashTableMap()
a[2] = 1
a[3] = 4
a[5] = 2
a[6] = 5
a[3] = 4
a[1] = 2
a[7] = 0
a[1] = 4
del a[1]

for elem in a:
    print(elem)
