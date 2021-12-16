def appearances(s, low, high):
    if low == high:
        res_dict = dict()
        res_dict.update({s[low] : 1})
        return res_dict

    else:
        temp_dict = appearances( s, low + 1, high )
        if temp_dict.get(s[low]) == None:
            temp_dict.update( {s[low]: 1} )
        else:
            temp_dict.update({s[low]: temp_dict.get(s[low])+1})
        return temp_dict

'''
        if appearances(s, low, high).get(s[low]) == None:
            print(s[low])
            appearances(s, low+1, high).update({s[low] : 1})
            return appearances(s, low+1, high)

        else:
            appearances( s, low+1, high).update({s[low]: appearances( s, low+1, high ).get(s[low+1])+1})
            print(s[low])
            return appearances(s, low+1, high)
'''

#print(appearances('Hello', 1,3))
