

def merge_sort(lst):
    if (len(lst) == 0):
        return
    elif (len(lst) == 1):
        return
    else:
        mid = (len(lst)) // 2
        left_lst = lst[ : mid]
        right_lst = lst[mid : ]
        merge_sort(left_lst)
        merge_sort(right_lst)
        merged = merge(left_lst, right_lst)
        for i in range(len(merged)):
            lst[i] = merged[i]

def merge(srt_lst1, srt_lst2):
    merged_list = []
    i1 = 0
    i2 = 0
    while ((i1 < len(srt_lst1)) and (i2 < len(srt_lst2))):
        if (srt_lst1[i1] < srt_lst2[i2]):
            merged_list.append(srt_lst1[i1])
            i1 += 1
        else:
            merged_list.append(srt_lst2[i2])
            i2 += 1
    while (i1 < len(srt_lst1)):
        merged_list.append(srt_lst1[i1])
        i1 += 1
    while (i2 < len(srt_lst2)):
        merged_list.append(srt_lst2[i2])
        i2 += 1
    return merged_list


def intersection_list(lst1, lst2):
    temp1 = lst1
    merge_sort(temp1) #[1,2,3,7,9]
    temp2 = lst2
    merge_sort(temp2) #[1,2,4,8]

    index1 = 0
    index2 = 0
    res = []

    while index1 < len(temp1) and index2 < len(temp2):
        if temp1[index1] == temp2[index2]:
            res.append(temp1[index1])
            index1 += 1
            index2 += 1
        elif temp1[index1] < temp2[index2]:
            index1 += 1
        elif temp1[index1] > temp2[index2]:
            index2 += 1
    return res



