from LinkedBinaryTree import LinkedBinaryTree

# 2 * (15-6 + 4)
def create_expression_tree(prefix_exp_str):
    lst = prefix_exp_str.split()
    def create_expression_subtree(lst,index):
        #print(lst[index])
        cursor = lst[index]
        if cursor not in '+-*/':
            root = LinkedBinaryTree.Node(int(cursor))
            return (root,index)
        else:
            left = create_expression_subtree(lst,index + 1)
            right = create_expression_subtree(lst,left[1]+1)
            root = LinkedBinaryTree.Node(cursor,left[0],right[0])
            return (root,right[1])
    return LinkedBinaryTree(create_expression_subtree(lst, 0)[0])


def prefix_to_postfix(prefix_exp_str):
    temp_tree = create_expression_tree(prefix_exp_str)
    postfix_exp_str = " ".join(str(node.data) for node in temp_tree.postorder())
    return postfix_exp_str


'''
t = create_expression_tree('* 2 + - 15 6 4')
for i in t.preorder():
    print(i.data)
'''