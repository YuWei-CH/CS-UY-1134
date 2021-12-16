from ArrayStack import ArrayStack

class MaxStack:
    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len( self ) == 0

    def push(self, val):
        if len(self.data) == 0:
            self.data.push((val,val))
        elif val > self.data.top()[-1]:
            self.data.push( (val,val) )
        else:
            self.data.push( (val, self.data.top()[-1]) )

    def pop(self):
        if (self.is_empty()):
            raise Exception( "Stack is empty" )
        temp = self.data.pop()
        return temp[0]

    def top(self):
        if (self.is_empty()):
            raise Exception( "Stack is empty" )
        return self.data.top()[0]

    def max(self):
        return self.data.top()[-1]


'''
maxS = MaxStack()
maxS.push(3)
maxS.push(1)
maxS.push(6)
maxS.push(4)
print(maxS.top())
print(maxS.max())
s = maxS.pop()
print(s)
maxS.pop()
print(maxS.max())
'''
