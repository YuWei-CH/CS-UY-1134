def count_lowercase(s,low,high):
    if low == high:
        if s[low].islower():
            return 1
        else:
            return 0
    else:
        if s[low].islower():
            return 1 + count_lowercase(s,low+1,high)
        elif s[high].islower():
            return 1 + count_lowercase(s, low, high-1)
        else:
            return 0 + count_lowercase(s, low+1,high-1)

'''        
s = 'HW' # 7
print(count_lowercase(s,0,8))
'''

def is_number_of_lowercase_even(s, low, high):
    if low == len(s):
        number = (high+1) - len(s)
        return number % 2 == 0
    else:
        if s[low].islower():
            s = s[:low]+s[low+1:]
            return is_number_of_lowercase_even( s, low, high )
        else:
            return is_number_of_lowercase_even( s, low+1, high )

'''
s = 'HWert' # 7
print(is_number_of_lowercase_even(s,0,4))

'''

