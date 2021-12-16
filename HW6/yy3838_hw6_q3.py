from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self,orig_str):
        self.data=DoublyLinkedList()
        if len(orig_str)!=0:
            temp = None
            for elem in orig_str:
                if elem != temp:
                    self.data.add_last((elem, 1))
                    temp = elem
                else:
                    number=self.data.delete_last()[1]
                    number+=1
                    self.data.add_last((temp,number))

                       
                

    def __add__(self,other):
        new_string = CompactString("")
        curr_node =self.data.header.next
        while(curr_node is not self.data.trailer):
            result=curr_node.data
            new_string.data.add_last((result))
            curr_node = curr_node.next
        if new_string.data.trailer.prev.data[0] == other.data.header.next.data[0]:
            new_string.data.trailer.prev.data = (new_string.data.trailer.prev.data[0],new_string.data.trailer.prev.data[1]+other.data.header.next.data[1])
            curr_node = other.data.header.next.next
        else:
            curr_node = other.data.header.next
        while(curr_node is not other.data.trailer):
            result=curr_node.data
            new_string.data.add_last((result))
            curr_node = curr_node.next

        return new_string

    def __lt__(self,other):
        temp1 = self.data.header.next
        temp2 = other.data.header.next
        while(True):
            if temp1==self.data.trailer and temp2!=other.data.trailer:
                return True
            elif temp1!=self.data.trailer and temp2==other.data.trailer:
                return False
            elif temp1==self.data.trailer and temp2==other.data.trailer:
                return False
            if temp1.data[0]<temp2.data[0]:
                return True
            elif temp1.data[0]>temp2.data[0]:
                return False
            else:
                if temp1.data[1]<temp2.data[1]:
                    temp1 = temp1.next
                elif temp1.data[1]>temp2.data[1]:
                    temp2 = temp2.next
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
    def __le__(self,other): 
        temp1 = self.data.header.next
        temp2 = other.data.header.next
        while(True):
            if temp1==self.data.trailer and temp2!=other.data.trailer:
                return True
            elif temp1!=self.data.trailer and temp2==other.data.trailer:
                return False
            elif temp1==self.data.trailer and temp2==other.data.trailer:
                return True
            if temp1.data[0]<temp2.data[0]:
                return True
            elif temp1.data[0]>temp2.data[0]:
                return False
            else:
                if temp1.data[1]<temp2.data[1]:
                    temp1 = temp1.next
                elif temp1.data[1]>temp2.data[1]:
                    temp2 = temp2.next
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
    def __gt__(self,other): 
        temp1 =self.data.header.next
        temp2 = other.data.header.next
        while(True):
            if temp1==self.data.trailer and temp2!=other.data.trailer:
                return False
            elif temp1!=self.data.trailer and temp2==other.data.trailer:
                return True
            elif temp1==self.data.trailer and temp2==other.data.trailer:
                return False
            if temp1.data[0]>temp2.data[0]:
                return True
            elif temp1.data[0]<temp2.data[0]:
                return False
            else:
                if temp1.data[1]<temp2.data[1]:
                    temp1 = temp1.next
                elif temp1.data[1]>temp2.data[1]:
                    temp2 = temp2.next
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
    def __ge__(self,other): 
        temp1 =self.data.header.next
        temp2 = other.data.header.next
        while(True):
            if temp1==self.data.trailer and temp2!=other.data.trailer:
                return False
            elif temp1!=self.data.trailer and temp2==other.data.trailer:
                return True
            elif temp1==self.data.trailer and temp2==other.data.trailer:
                return True
            if temp1.data[0]>temp2.data[0]:
                return True
            elif temp1.data[0]<temp2.data[0]:
                return False
            else:
                if temp1.data[1]<temp2.data[1]:
                    temp1 = temp1.next
                elif temp1.data[1]>temp2.data[1]:
                    temp2 = temp2.next
                else:
                    temp1 = temp1.next
                    temp2 = temp2.next
    def __repr__(self):
        result = ""
        cursor = self.data.header
        for i in range(len(self.data)):
            elem = cursor.next.data[0]
            count = cursor.next.data[1]
            for j in range(count):
                result = result + elem
            cursor = cursor.next
        return result

s3 = CompactString('aaabbbbcc')
s4 = CompactString('ccaaa')
s5 = s3+s4
print(s3)
print(s4)
print(s5,'xxxsxs')

print(s3 > s4,'jhj')
print(s3 <= s4,'345')
print(s3 < s4,'jhj')
print(s3 >= s4,'jhj')