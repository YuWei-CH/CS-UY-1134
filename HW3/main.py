def find_duplicates(lst):
    length = len( lst )

    dupVal = []

    for i in range( 0, length ):
        index = lst[i] % length
        if (lst[index] >= length):

            if (lst[index] < 2 * length):
                dupVal.append( index )

        lst[index] =  lst[index] + length

    return dupVal
lst=[2,2,2,2,2,2,5,6,7,3,3] #6
print(find_duplicates(lst))