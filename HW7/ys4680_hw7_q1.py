from LinkedBinaryTree import LinkedBinaryTree
def min_and_max(bin_tree):
    def subtree_min_and_max(root):
        #print(root.data,'1111')
        if root.left is None and root.right is None:
            #print( root.data, '2222' )
            return (root.data,root.data)
        elif root.left is not None and root.right is None:
            #print( root.data, '3333' )
            temp = subtree_min_and_max(root.left)
            return (min(temp[0],root.data),max(temp[1],root.data))
        elif root.left is None and root.right is not None:
            #print( root.data, '4444' )
            temp = subtree_min_and_max(root.right)
            return (min(temp[0],root.data),max(temp[1],root.data))
        else:
            #print( root.data, '5555' )
            left = subtree_min_and_max(root.left)
            right = subtree_min_and_max(root.right)
            return (min(left[0],right[0],root.data),max(left[1],right[1],root.data))
    if bin_tree.root is None:
        raise Exception( 'Empty Tree' )
    return subtree_min_and_max(bin_tree.root)


'''
a = LinkedBinaryTree.Node(5)
b = LinkedBinaryTree.Node(4)
c = LinkedBinaryTree.Node(6, a, b)
d = LinkedBinaryTree.Node(8)
e = LinkedBinaryTree.Node(10, None, d)
f = LinkedBinaryTree.Node(12, e, c)
t = LinkedBinaryTree(f)

print(min_and_max(t))
'''