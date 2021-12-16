def list_min(lst, low, high):
    if (low == high):
        return lst[low]
    else:
        mid = (low + high) // 2
        min1 = list_min( lst, low, mid )
        min2 = list_min( lst, mid + 1, high )
        if (min1 < min2):
            return min1
        else:
            return min2
'''
lst =[4,22,4,6,3,5]
print(list_min(lst,0,5))
'''



