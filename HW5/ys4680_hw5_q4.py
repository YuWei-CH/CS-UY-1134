from ArrayStack import ArrayStack


class Queue:
    def __init__(self):
        self.stack1 = ArrayStack()
        self.stack2 = ArrayStack()
        self.n = 0

    def __len__(self):
        return self.n

    def is_empty(self):
        return (self.n == 0)

    def first(self):
        if len( self.stack1 ) == 0 and len( self.stack2 ) == 0:
            raise Exception( 'Empty Queue' )

        elif len( self.stack2 ) == 0 and len( self.stack1 ) > 0:
            self.n -= 1
            while len( self.stack1 ):
                temp = self.stack1.pop()
                self.stack2.push( temp )
            return self.stack2.top()

        else:
            self.n -= 1
            return self.stack2.top()


    def enqueue(self, x):
        self.n += 1
        self.stack1.push( x )

    def dequeue(self):
        if len( self.stack1 ) == 0 and len( self.stack2 ) == 0:
            raise Exception( 'Empty Queue' )

        elif len( self.stack2 ) == 0 and len( self.stack1 ) > 0:
            self.n -= 1
            while len( self.stack1 ):
                temp = self.stack1.pop()
                self.stack2.push( temp )
            return self.stack2.pop()

        else:
            self.n -= 1
            return self.stack2.pop()

'''
temp = Queue()
temp.enqueue(1)
temp.enqueue(2)
temp.enqueue(3)
print(temp.dequeue())
print(temp.dequeue())
print(len(temp.stack2))
temp.enqueue(4)
print(temp.stack1.top())
print(temp.dequeue())
'''