from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    cursor_first = srt_lnk_lst1.header.next
    cursor_second = srt_lnk_lst2.header.next
    def merge_sublists(first, second):
        if first.data is None and second.data is None:
            result = DoublyLinkedList()
            return result

        elif first.data is None and second.data is not None:
            temp = merge_sublists(first,second.next)
            # print( temp,'%' )
            temp.add_first(second.data)
            return temp

        elif second.data is None and first.data is not None:
            temp = merge_sublists(second,first.next)
            # print( temp, '*' )
            temp.add_first(first.data)
            return temp

        else:

            if first.data < second.data:
               # print(first.data)

                temp = merge_sublists( first.next, second )
                # print( temp, '$' )
                temp.add_first( first.data )
                return temp


            else:

               # print( first.data )
                temp = merge_sublists( first, second.next )
                # print( temp, '@' )
                temp.add_first( second.data )
                return temp

    return merge_sublists(cursor_first,cursor_second)

'''
test1 = DoublyLinkedList()
test2 = DoublyLinkedList()
test1.add_last(1)
test1.add_last(3)
test1.add_last(5)
test1.add_last(6)
test1.add_last(8)

test2.add_last(2)
test2.add_last(3)
test2.add_last(5)
test2.add_last(10)
test2.add_last(15)
test2.add_last(18)



print(merge_linked_lists(test1,test2))

'''