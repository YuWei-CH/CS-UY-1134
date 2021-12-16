import random
from UnsortedArrayMap import UnsortedArrayMap

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

    class Item:
        def __init__(self, key, value = None):
            self.key = key
            self.value = value

    def __init__(self, N=64):
        self.table = make_array(N)
        for i in range(N):
            self.table[i] = None
        self.n = 0
        self.h = ChainingHashTableMap.MADHashFunction(N)


    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.h(key) #返回一个index
        curr_bucket = self.table[i]

        if curr_bucket is None:
            raise KeyError('No such Key')

        elif isinstance(curr_bucket,UnsortedArrayMap):
            try:
                return curr_bucket[key]
            except KeyError:
                raise KeyError('No such Key')
        else:
            if key == curr_bucket.key:
                return curr_bucket.value
            else:
                raise KeyError( 'No such Key' )


    def __setitem__(self, key, value):
        i = self.h(key)
        curr_bucket = self.table[i]
        if curr_bucket is None:
            self.table[i] = ChainingHashTableMap.Item(key,value)
            self.n += 1
        elif isinstance(curr_bucket,ChainingHashTableMap.Item):
            if curr_bucket.key == key:
                curr_bucket.value = value
            else:
                temp = UnsortedArrayMap()
                temp[curr_bucket.key] = curr_bucket.value
                temp[key] = value
                self.table[i] = temp
                self.n += 1
        else:
            old_size = len( curr_bucket )
            curr_bucket[key] = value
            new_size = len(curr_bucket)
            if (new_size > old_size):
                self.n += 1 #判断在UnsortedArrayMap里面是mutate了还是append了
            if (self.n > len(self.table)):
                self.rehash(2 * len(self.table))

    def __delitem__(self, key):
        i = self.h(key)
        curr_bucket = self.table[i]
        res = None
        if curr_bucket is None:
            raise KeyError('No such Key')
        elif isinstance(curr_bucket,ChainingHashTableMap.Item):
            self.n -= 1
            res = curr_bucket
            self.table[i] = None
            return res
        else:
            del curr_bucket[key]
            self.n -= 1
            if (self.n < len( self.table ) // 4):
                self.rehash( len( self.table ) // 2 )

    def __contains__(self, key):
        try:
            val = self[key]
            return True
        except KeyError:
            return False

    def __iter__(self):
        for curr_bucket in self.table:
            if curr_bucket is None:
                pass
            elif isinstance(curr_bucket,ChainingHashTableMap.Item):
                yield curr_bucket.key
            else:
                for item in curr_bucket:
                    yield item

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val

'''
test = ChainingHashTableMap()
test[1] = 1
test[1] = 10
test[2] = 2
test[3] = 3
del test[2]
test[4] = 4
test[5] = 5

for item in test:
    print(test[item])
'''