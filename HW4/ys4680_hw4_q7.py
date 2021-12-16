def split_by_sign(lst, low, high):
    if low == high:
        return lst
    else:
        if lst[low] > 0 and lst[high] < 0:
            lst[low],lst[high] = lst[high],lst[low]
            return split_by_sign(lst, low, high)

        elif lst[high] > 0 and lst[high] > 0:
            return split_by_sign( lst, low, high - 1 )

        elif lst[low] < 0 and lst[high] > 0:
            return split_by_sign( lst, low+1, high )
        else:
            return split_by_sign(lst, low+1, high)


'''
lst = [-1,-1,2,-3,2,-6]
[1,-1,2]
[-1,1,2]
print(split_by_sign(lst,0,5))
'''
# 1,-1,2,0,0,-3,2