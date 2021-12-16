from ArrayList import ArrayList

class ArrayStack:
    def __init__(self):
        self.data = ArrayList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Exception("Stack is empty")
        return self.data.pop()


def stack_sum(s):
    if len(s) == 1:
        return s.top()
    else:
        a = s.top()
        s.pop()
        result = stack_sum(s) + a
        s.push(a)
        return result

'''
s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(stack_sum(s))
'''


def eval_prefix(exp_str):
    exp_lst = exp_str.split(' ')
    exp_stack = ArrayStack()
    for i in exp_lst[-1::-1]:
        if i.isdigit():
            exp_stack.push(int(i))
        elif i in '+-*/':
            temp1\
                = exp_stack.pop()
            temp2 = exp_stack.pop()
            if i == '+':
                res = temp1 + temp2
            elif i == '-':
                res = temp1 - temp2
            elif i == '*':
                res = temp1 * temp2
            elif i == '/':
                if temp2 == 0:
                    raise ZeroDivisionError
                else:
                    temp1 / temp2
            exp_stack.push( res )
    return exp_stack.pop()
'''
exp_str = "- + * 16 5 * 8 4 20"
print(eval_prefix(exp_str))
'''
def flatten_list(lst):
    s = ArrayStack()
    for i in lst:
        s.push(i)
    for i in range(len(lst)):
        lst.pop()
    while len(s) > 0:
        temp = s.pop()
        if isinstance(temp,int):
            print(temp)
            lst.insert(0,temp)
        elif isinstance(temp,list) and len(temp) == 1:
            s.push(temp[0])
        else:
            remain2 = temp[-1]
            remain1 = temp[0:-1]
            s.push(remain1)
            s.push(remain2)
    return lst


lst = [[[[0]]], [1, 2], 3, [4, [5, 6, [7]], 8], 9]
asd = flatten_list(lst)
print(asd)

