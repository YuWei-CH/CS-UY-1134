from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for i in num_str:
            self.data.add_last(int(i))

    def __add__(self, other):

        result = Integer('0')
        result.data.delete_last()
        for i in self.data:
            result.data.add_last(i)

        cursor_self = result.data.trailer.prev
        cursor_other = other.data.trailer.prev
        if len(result.data) is not len(other.data):
            if len(result.data) < len(other.data):
                for i in range(len(other.data) - len(result.data)):
                    result.data.add_first(0)

        while cursor_other.data is not None and cursor_self.data is not None:

            '''
            print( cursor_self.data, 'before' )
            print( cursor_other.data, 'before' )
            '''

            if cursor_self.data is None or cursor_other.data is None:
                result.data.add_first(0)
            elif cursor_self.data + cursor_other.data >= 10:
                value = cursor_self.data + cursor_other.data - 10
                cursor_self.data = value
                if cursor_self.prev.data is None:
                    result.data.add_first(1)
                else:
                    cursor_self.prev.data += 1
                    while cursor_self.prev.data is not None and cursor_self.prev.data == 10:
                        if cursor_self.prev.prev.data == None and cursor_self.prev.data == 10:
                            result.data.add_first(0)
                        cursor_self.prev.data = 0
                        cursor_self.prev.prev.data += 1
                        cursor_self = cursor_self.prev
            else:
                cursor_self.data = cursor_self.data + cursor_other.data

            '''
            print(cursor_self.data,'then')
            print( cursor_other.data,'then' )
            '''

            cursor_self = cursor_self.prev
            cursor_other = cursor_other.prev


        return result


    def __repr__(self):

        if self.data.header.next.data == 0 and len(self.data) == 1:
            return '0'
        else:
            result = ''
            temp = True
            for i in self.data:
                if i != 0:
                    temp = False
                if i == 0 and temp:
                    continue
                result = result + str(i)
            return result

    def __mul__(self, other):
        ff = Integer('0')
        result = Integer( '0' )
        result.data.delete_last()
        for i in self.data:
            result.data.add_last( i )
        counter = len(other.data)-1
        cursor = other.data.header.next
        while cursor.data is not None:
            ss = Integer( '0' )
            ss.data.delete_last()
            for i in self.data:
                ss.data.add_last( i )
            temp_result = Integer( '0' )
            temp_result.data.delete_last()
            for i in self.data:
                temp_result.data.add_last( i )
            for j in range(counter):
                ss.data.add_last(0)
            counter -= 1
            final_result = Integer( '0' )
            for i in range(cursor.data):
                final_result = final_result + ss
            cursor = cursor.next
            ff = ff + final_result
        return ff





'''
a = Integer('9999')
b = Integer('1')
c = a + b
d = b + a
print(c)
print(d)
'''

'''
a = Integer('12')
b = Integer('0')
c = a * b
print(c)
'''