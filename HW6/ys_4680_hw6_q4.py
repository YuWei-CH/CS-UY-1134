from DoublyLinkedList import DoublyLinkedList

def copy_linked_list(lnk_lst):
    copy_linklist = DoublyLinkedList()
    cursor_origen = lnk_lst.header.next
    while cursor_origen.data is not None:
        copy_linklist.add_last(cursor_origen.data)
        cursor_origen = cursor_origen.next
    return copy_linklist

'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)
lnk_lst2 = copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10
e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data)
'''


def deep_copy_linked_list(lnk_lst):
    copy_linklist = DoublyLinkedList()
    cursor = lnk_lst.header.next

    while cursor.data is not None:
        if isinstance(cursor.data,int):
            copy_linklist.add_last( cursor.data)

        else:
            copy_linklist.add_last(deep_copy_linked_list( lnk_lst.header.next.data))
        cursor = cursor.next

    return copy_linklist


'''
lnk_lst1 = DoublyLinkedList()
elem1 = DoublyLinkedList()
elem1.add_last(1)
elem1.add_last(2)
lnk_lst1.add_last(elem1)
elem2 = 3
lnk_lst1.add_last(elem2)
lnk_lst2 = deep_copy_linked_list(lnk_lst1)
e1 = lnk_lst1.header.next
e1_1 = e1.data.header.next
e1_1.data = 10
e2 = lnk_lst2.header.next
e2_1 = e2.data.header.next
print(e2_1.data)
'''