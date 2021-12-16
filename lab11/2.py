from LinkedBinaryTree import LinkedBinaryTree
from ArrayStack import ArrayStack
a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
t = LinkedBinaryTree(f)

def bt_even_sum(root):
    if root.left is None and root.right is None:
        if root.data % 2 == 0:
            return root.data
        else:
            return 0
    elif root.left is None and root.right is not None:
        right = bt_even_sum(root.right)
        if root.data % 2 == 0:
            return root.data + right
        else:
            return right
    elif root.left is not None and root.right is None:
        left = bt_even_sum(root.left)
        if root.data % 2 == 0:
            return root.data + left
        else:
            return left
    else:
        left = bt_even_sum(root.left)
        right = bt_even_sum(root.right)
        if root.data % 2 == 0:
            return root.data + left +right
        else:
            return left + right
#print(bt_even_sum(f))

def bt_contains(root,val):
    if root.left is None and root.right is None:
        if root.data != val:
            return False
        else:
            return True
    elif root.left is None and root.right is not None:
        if root.data != val:
            right = bt_contains(root.right,val)
            return right
        else:
            return True
    elif root.left is not None and root.right is None:
        if root.data != val:
            left = bt_contains(root.left,val)
            return left
        else:
            return True
    else:
        left = bt_contains(root.left,val)
        right = bt_contains( root.right, val )
        if root.data != val:
            return left or right
        else:
            return True
#print(bt_contains(f,5))

def is_full(root):
    if root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        return False
    elif root.left is not None and root.right is  None:
        return False
    else:
        left = is_full(root.left)
        right = is_full(root.right)
        return left and right

#print(is_full(A))


def invert_bt(root):
    if root.left is  None and root.right is   None:
        root.left,root.right = root.right,root.left
    elif root.left is None and root.right is not None:
        root.left,root.right = root.right,root.left
    elif root.left is not None and root.right is None:
        root.left, root.right = root.right, root.left
    else:
        root.left,root.right = root.right,root.left
        invert_bt(root.left)
        invert_bt(root.right)

F = LinkedBinaryTree.Node( 9 )
G = LinkedBinaryTree.Node( 11 )
E = LinkedBinaryTree.Node(4)
D = LinkedBinaryTree.Node(1,F,G)
B = LinkedBinaryTree().Node(3)
C = LinkedBinaryTree.Node(6,D,E)
A = LinkedBinaryTree().Node(7,B,C)
invert_bt(A)
tree = LinkedBinaryTree(A)
#for i in tree.breadth_first():
    #print(i.data)

def preorder_with_stack(self):
    stack = ArrayStack()
    stack.push(self.root)
    while not stack.is_empty():
        temp = stack.pop()
        if temp.left is not None:
            stack.push(temp.left)
        if temp.right is not None:
            stack.push(temp.right)
        yield temp.data

a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
t = LinkedBinaryTree(f)

for item in preorder_with_stack(t):
    print(item)



