class DoublyLinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
            self.prev = None

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None


    def __init__(self):
        self.header = DoublyLinkedList.Node() # a node with Note prev, None data, None next
        self.trailer = DoublyLinkedList.Node() #
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def add_after(self, node, val):
        new_node = DoublyLinkedList.Node(val)
        prev_node = node
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        next_node.prev = new_node
        new_node.next = next_node
        self.size += 1
        return new_node

    def add_first(self, val):
        return self.add_after(self.header, val)

    def add_last(self, val):
        return self.add_after(self.trailer.prev, val) #保证一直在trailer前

    def add_before(self, node, val):
        return self.add_after(node.prev, val) # node前面

    def delete_node(self, node): # 绕过了这个node
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def delete_first(self):
        if(self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.header.next) #直接把header和后面node的连接起来
 
    def delete_last(self):
        if(self.is_empty() == True):
            raise Exception("List is empty")
        return self.delete_node(self.trailer.prev) #把node和trailer链接了

    def __iter__(self):
        cursor = self.header.next
        while(cursor is not self.trailer): #循环untill trailer
            yield cursor.data
            cursor = cursor.next

    def __repr__(self):
        return "[" + " <--> ".join([str(elem) for elem in self]) + "]"

