import random
from UnsortedArrayMap import UnsortedArrayMap
from DoublyLinkedList import DoublyLinkedList
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
            self.table[i] = DoublyLinkedList()
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)


    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, index):
        i = self.h(index) #返回一个index
        curr_bucket = self.table[i]
        for i in curr_bucket:
            if i is

    def __setitem__(self, value):
        i = self.h(value)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.n += 1 #判断在UnsortedArrayMap里面是mutate了还是append了
        if (self.n > len(self.table)):
            self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
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
        for curr_bucket in self.table:
            for key in curr_bucket:
                yield key

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val
