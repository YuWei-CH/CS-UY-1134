from DoublyLinkedList import DoublyLinkedList


class CompactString:


    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        counter = 1
        for i in range(len(orig_str)):

            if i == 0:
                self.data.add_last((counter,orig_str[i]))
            elif i > 0 and orig_str[i] == self.data.trailer.prev.data[1]:
                counter += 1
                self.data.trailer.prev.data = (counter,orig_str[i])
            else:
                counter = 1
                self.data.add_last( (counter, orig_str[i]) )

    def __add__(self, other):
        result = CompactString( '0' )
        for i in self.data:
            result.data.add_last( i )
        result.data.delete_first()

        oth = CompactString( '0' )
        for i in other.data:
            oth.data.add_last( i )
        oth.data.delete_first()

        if result.data.trailer.prev.data[1] is oth.data.header.next.data[1]:
            result.data.trailer.prev.data = (result.data.trailer.prev.data[0] + oth.data.header.next.data[0], oth.data.delete_first()[1])
        for j in  oth.data:
            result.data.add_last(j)
        return result

    def __lt__(self, other):
        if len(other.data) == 0:
            return False
        # print(self,other,'1')
        cursor_self = self.data.header.next
        cursor_other = other.data.header.next

        while cursor_self.data is cursor_other.data:
            cursor_self = cursor_self.next
            cursor_other = cursor_other.next
        if cursor_self.next.data is None or cursor_other.next.data is None:
            return cursor_self.data[0] < cursor_other.data[0]
        else:
            if cursor_self.data[0] < cursor_other.data[0]:
                if cursor_self.next.data[1] < cursor_other.data[1]:
                    return True
                else:
                    return False
            else:
                if cursor_self.data[1] < cursor_other.next.data[1]:
                    return True
                else:
                    return False


    def __le__(self, other):
        # print( self, other ,'2')
        cursor_self = self.data.header.next
        cursor_other = other.data.header.next
        while cursor_self is not None and cursor_other is not None and cursor_self.data == cursor_other.data :
            cursor_self = cursor_self.next
            cursor_other = cursor_other.next
        if cursor_self is None and cursor_other is None:
            return True
        else:
            return self < other

    def __gt__(self, other):
        # print( self, other ,'3')
        return not (self <= other)

    def __ge__(self, other):
        # print( self, other,'4' )
        return  not (self < other)

    def __repr__(self):
        result = ''
        cursor = self.data.header.next
        for i in self.data:
            result = result + (cursor.data[0] * cursor.data[1])
            cursor = cursor.next
        return result






'''
s3 = CompactString('aaa')
s4 = CompactString('')
print(s3)
print(s4)

print(s3 > s4,'jhj')
print(s3 <= s4,'345')
print(s3 < s4,'jhj')
print(s3 >= s4,'jhj')
'''
