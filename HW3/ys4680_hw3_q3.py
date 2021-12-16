def find_duplicates(lst):
    temp = []
    Max = 0
    dup_list = []
    for j in lst:
        if j > Max:
            Max = j
    for i in range(Max+1):
        temp.append(0)

    for i in lst:
        temp[i] += 1
    for i in range(len(temp)):
        if temp[i] > 1:
            dup_list.append(i)
    return dup_list

