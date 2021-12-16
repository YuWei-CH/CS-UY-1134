def nested_sum(lst):
    if len(lst) == 1 and isinstance(lst, int):
        if isinstance(lst, list):
            temp = 0
            i = 0
            while i < len(lst)-1:
                temp += lst[i]
                i += 1
            return i
        elif isinstance(lst, int):
            return lst
    else:
        if len(lst) == 1:
            lst = lst[0]
        print( lst )
        if isinstance(lst[0], list):
            temp = 0
            i = 0
            while i < len( lst[0])  - 1:
                temp += lst[0][i]
                i += 1
            return  temp + nested_sum( lst[1:] )

        elif isinstance(lst[0], int):
            return lst[0] + nested_sum( lst[1:] )

lst = [ [1, 2], 3, [4, [5, 6, [7], 8 ] ] ]
nested_sum(lst)