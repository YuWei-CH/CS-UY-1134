def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst)-1
    while left < right:
        mid = srt_lst[left] + srt_lst[right]
        if mid == target:
            return (left, right)
        elif mid > target:
            right = right - 1
        elif mid < target:
            left = left + 1
    return None








