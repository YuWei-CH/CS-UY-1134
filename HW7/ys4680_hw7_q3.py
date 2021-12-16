from LinkedBinaryTree import LinkedBinaryTree


def is_height_balanced(bin_tree):
    def is_subtree_high_balanced(subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return (True, 1)
        elif subtree_root.left is None and subtree_root.right is not None:
            right = is_subtree_high_balanced(subtree_root.right)
            if right[1] == 1:
                return (right[0],right[1]+1)
            else:
                return (False,0)

        elif subtree_root.left is not None and subtree_root.right is None:
            left = is_subtree_high_balanced(subtree_root.left)
            if left[1] == 1:
                return (left[0],left[1]+1)
            else:
                return (False,0)

        else:
            left = is_subtree_high_balanced(subtree_root.left)
            right = is_subtree_high_balanced(subtree_root.right)
            if abs(left[1] - right[1]) <= 1:
                return (True,left[1]+right[1])
            else:
                return (False,0)
    return is_subtree_high_balanced(bin_tree.root)[0]
'''
a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(1)
c = LinkedBinaryTree.Node(8, a, b)
d = LinkedBinaryTree.Node(4)
e = LinkedBinaryTree.Node(7, c, d)
f = LinkedBinaryTree.Node(9)
g = LinkedBinaryTree.Node(2, f, None)
h = LinkedBinaryTree.Node(3, g, e)

bin_tree = LinkedBinaryTree(h)

print(is_height_balanced(bin_tree))

i = LinkedBinaryTree.Node(5)
j = LinkedBinaryTree.Node(1)
k = LinkedBinaryTree.Node(9, i, j)
l = LinkedBinaryTree.Node(2, k, None)
m = LinkedBinaryTree.Node(8)
n = LinkedBinaryTree.Node(4)
o = LinkedBinaryTree.Node(7, m, n)
p = LinkedBinaryTree.Node(3, l, o)

bin_tree_2 = LinkedBinaryTree(p)

print(is_height_balanced(bin_tree_2))
'''



