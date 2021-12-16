from ArrayQueue import ArrayQueue

class LinkedBinaryTree:

    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            if (self.left is not None):
                self.left.parent = self
            self.right = right
            if (self.right is not None):
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.count_nodes()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0


    def count_nodes(self):
        def subtree_count(root):
            if (root is None):
                return 0
            else:
                left_count = subtree_count(root.left)
                right_count = subtree_count(root.right)
                return 1 + left_count + right_count

        return subtree_count(self.root)


    def sum(self):
        def subtree_sum(root):
            if (root is None):
                return 0
            else:
                left_sum = subtree_sum(root.left)
                right_sum = subtree_sum(root.right)
                return root.data + left_sum + right_sum

        return subtree_sum(self.root)


    def height(self):
        def subtree_height(root):
            if (root.left is None and root.right is None): #终止本段的寻找
                return 0
            elif (root.left is None):
                return 1 + subtree_height(root.right) #目前左边的长度
            elif (root.right is None):
                return 1 + subtree_height(root.left) #目前右边的长度
            else:
                left_height = subtree_height(root.left) #左下寻找
                right_height = subtree_height(root.right) #右下寻找
                return 1 + max(left_height, right_height) # value的增加

        if(self.is_empty()):
            raise Exception("Tree is empty")
        return subtree_height(self.root)


# deepth first search：

    def preorder(self): # current > left > right
        def subtree_preorder(root):
            if (root is None):
                pass
            else:
                yield root
# yield from X : for i in X:
#                   yield i
                yield from subtree_preorder(root.left)
                yield from subtree_preorder(root.right)

        yield from subtree_preorder(self.root)


    def postorder(self): # left > right > root
        def subtree_postorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_postorder(root.left)
                yield from subtree_postorder(root.right)
                yield root

        yield from subtree_postorder(self.root)


    def inorder(self):
        def subtree_inorder(root):
            if (root is None):
                pass
            else:
                yield from subtree_inorder(root.left)
                yield root
                yield from subtree_inorder(root.right)

        yield from subtree_inorder(self.root)

# breath first search
    def breadth_first(self):
        if (self.is_empty()):
            return
        line = ArrayQueue()
        line.enqueue(self.root)
        while (line.is_empty() == False):
            curr_node = line.dequeue()
            yield curr_node
            if (curr_node.left is not None):
                line.enqueue(curr_node.left)
            if (curr_node.right is not None):
                line.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data



a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
t = LinkedBinaryTree(f)

for i in t.preorder():
    print(i.data)

print('******************')

for i in t.postorder():
    print(i.data)

print('******************')

for i in t.inorder():
    print(i.data)

print('******************')

for i in t.breadth_first():
    print(i.data)

