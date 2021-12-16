from ArrayQueue import ArrayQueue
from ArrayStack import ArrayStack
from LinkedBinaryTree import LinkedBinaryTree

def bt_even_sum(root):
    if root is None:
        return 0
    else:
            left = bt_even_sum(root.left)
            right = bt_even_sum(root.right)
            if root.data % 2 == 0:
                return left + right + root.data
            else:
                return left + right


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
t = LinkedBinaryTree(f)

#print(bt_even_sum(f))

def bt_contains(root, val):
    if root is not None:
        if root.data == val:
            return True
        else:
            print(root.data)
            bt_contains(root.left,val)
            bt_contains(root.right,val)
    return False
print(bt_contains(f,4))

def is_full(root):
    if root is not None:
        print(root.data)
        if root.left is None and root.right is not None:
            return False
        elif root.left is not None and root.left is None:
            return False
        else:
            is_full(root.left)
            is_full(root.right)
        return True


F = LinkedBinaryTree.Node( 9 )
G = LinkedBinaryTree.Node( 11 )
E = LinkedBinaryTree.Node(4)
D = LinkedBinaryTree.Node(1,F,G)
B = LinkedBinaryTree().Node(3)
C = LinkedBinaryTree.Node(6,D,E)
A = LinkedBinaryTree().Node(7,B,C)
tree = LinkedBinaryTree(A)
#print(is_full(A))


def invert_bt(root):
    if root is not None:
        root.left,root.right = root.right,root.left
        invert_bt(root.left)
        invert_bt(root.right)

print(invert_bt(A))
for i in tree.breadth_first():
    print(i.data)

def invert_bt_n(root):
    queue = ArrayQueue()

    queue.enqueue(root)
    while queue.is_empty() == False:
        node = queue.dequeue()

        node.left, node.right = node.right, node.left
        # node 的left 和 right都是None的话就不会被添加进来
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

#print(invert_bt_n(A))
#for i in tree.breadth_first():
    #print(i.data)


def preorder_with_stack(self):
    stack = ArrayStack()
    if self.root is not None:
        stack.push(self.root)
    while stack.is_empty() == False:
        temp_node = stack.pop()
        if temp_node.right is not None:
            stack.push(temp_node.right)
        if temp_node.left is not None:
            stack.push( temp_node.left )
        yield temp_node.data


a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
t = LinkedBinaryTree(f)
'''
for item in preorder_with_stack(t):
    print(item, end = ' ')
    print()
'''



