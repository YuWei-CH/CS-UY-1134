'''
def flat_list(nested_lst, low, high):
    if low == len(nested_lst):
        lst = []
        for i in range(high+1):
            if isinstance(nested_lst[i],int) :
                lst.append(nested_lst[i])
        return lst

    else:
        if isinstance(nested_lst[low],list) and len(nested_lst[low]) == 1:
            nested_lst[low] = nested_lst[low][0]
            return flat_list( nested_lst, low , high )
        elif isinstance(nested_lst[low],list):
            nested_lst.insert(low,nested_lst[low][0])
            nested_lst[low+1].pop(0)
            high += 1
            return flat_list(nested_lst, low, high)
        elif isinstance(nested_lst[low], int):
            return flat_list( nested_lst, low + 1, high )
'''

def flat_list(nested_lst, low, high):
    if low > high:
        return []
    else:
        if isinstance( nested_lst[low], list ):
            return flat_list( nested_lst[low], 0, len( nested_lst[low] ) - 1 ) + flat_list( nested_lst, low + 1, high )
        return [nested_lst[low]] + flat_list( nested_lst, low + 1, high )
'''
nested_lst=[[1, 2], 3, [4, [5, 6, [7], 8]]]
print(flat_list(nested_lst,0,2))
'''