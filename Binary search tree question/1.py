from BinarySearchTreeMap import BinartSearchTreeMap

def create_chain_bst(n):
    Tree = BinartSearchTreeMap()
    i = 1
    while  i > n:
        Tree.insert(i,None)
        i += 1
    return Tree

def add_items(tree,low,high):
    mid = (low + high) // 2
    if low == high:
        tree.insert(low,None)
    else:
        tree.insert( mid, None )
        add_items(tree,low,mid-1)
        add_items(tree,mid+1,high)


def create_complete_bst(n):
    bst =BinartSearchTreeMap()
    add_items(bst, 1, n)
    return bst

'''
create_complete_bst(7)
for i in create_complete_bst(7).inorder():
    print(i.item.key)
'''

def restore_bst(prefix_lst):
   root = BinartSearchTreeMap.Node(prefix_lst[0])
   for i in range(len(prefix_lst)[1:-1]):
       node = BinartSearchTreeMap.Node(prefix_lst[i])
       if prefix_lst[i] > prefix_lst[i-1]:
           node

print()




def restore_bst(prefix_lst):
    # returns tuples containing the connect position and current node
    def restore_bst_helper(prefix_lst, start_pos, val_to_insert):
        new_item = BinartSearchTreeMap.Item(prefix_lst[start_pos])
        curr_node = BinartSearchTreeMap.Node(new_item)  # create subtrees leaning to left
        if start_pos == 0:
            return curr_node, curr_node
        connect_pos = None
        while prefix_lst[start_pos] < prefix_lst[start_pos - 1]:
            start_pos -= 1
            prev_node = curr_node
            new_item = BinartSearchTreeMap.Item(prefix_lst[start_pos])
            curr_node = BinartSearchTreeMap.Node(new_item)
            if val_to_insert is not None and curr_node.item.key > val_to_insert and connect_pos is None:
                connect_pos = prev_node
            curr_node.left = prev_node
            prev_node.parent = curr_node
            if start_pos == 0:
                if connect_pos is None:  # if connect position is None, then the connect position should be the root of the subtree
                    return curr_node, curr_node
                return connect_pos, curr_node
        prev_connect_pos, curr_root = restore_bst_helper(
            prefix_lst, start_pos - 1, curr_node.item.key)
        prev_connect_pos.right = curr_node
        # connect current subtree to the returned subtree
        curr_node.parent = prev_connect_pos
        if connect_pos is None:
            connect_pos = curr_node
        if val_to_insert is not None and val_to_insert > curr_root.item.key > connect_pos.item.key:
            # process the edge case in which current subtree should connect to the root
            return curr_root, curr_root
        return connect_pos, curr_root
    bst = BinartSearchTreeMap()
    if len(prefix_lst) == 0:
        return bst
    bst.root = restore_bst_helper(prefix_lst, len(prefix_lst) - 1, None)[1]
    bst.size = len(prefix_lst)
    return bst

#for i in restore_bst([9, 7, 3, 1, 5, 13, 11, 15]).inorder():
    #print(i.item.key)



#def find_min_abs_difference(bst):


def restore_bst(prefix_lst):
    tree = BinartSearchTreeMap()
    item = BinartSearchTreeMap.Item( prefix_lst[0], None )
    node = BinartSearchTreeMap.Node( item )
    tree.root = node
    def restore_bst_helper(prefix_lst,index,node):
        if index >= len(prefix_lst)-1:
            return
        else:
            item = BinartSearchTreeMap.Item( prefix_lst[index+1], None )
            node = BinartSearchTreeMap.Node(item)
            if prefix_lst[index+1] <= node.item.key:
                node.left = restore_bst_helper(prefix_lst,index+1,node)
                return node.left
            if prefix_lst[index+1] > node.item.key:
                node.right = restore_bst_helper(prefix_lst,index+1,node)
                return node.right
    restore_bst_helper(prefix_lst,0,tree.root)
    return tree

for i in restore_bst([9, 7, 3, 1, 5, 13, 11, 15]).inorder():
    print(i.item.key)


