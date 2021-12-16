
def shift(lst, k, direction = "left"):
    if direction == "left":
        for i in range(k):
            lst.append(lst[i])
        del lst[0:k]
    else:
        length = len(lst)-k
        for i in range(length):
            lst.append( lst[i] )
        del lst[0:length]

    def shift(lst, k):
        for i in range( k ):
            lst.append( lst[i] )
        del lst[0:k]

        