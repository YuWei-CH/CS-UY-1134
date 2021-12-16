def sum_to(n):
    if n == 1:
        return n
    else:
        return n+sum_to(n-1)
print(sum_to(5))

def product_evens(n):
        if n < 2:
            return 1
        if n % 2 != 0:
            n -= 1
        if n == 2:
            return 2
        else:
                return n * product_evens(n-2)
print(product_evens(9))

def find_max(lst,low,high):
    if low == high:
        return lst[0]  # base case
    else:
        prev = find_max(lst,low+1,high)
        if prev > lst[low+1]:
            return prev
        return lst[low+1]
lst = [13, 9, 16, 3, 4, 2]
print(find_max(lst,0,len(lst)-1))

def is_palindrome(input_str, low, high):
    if low + high == len(input_str)-1:
        if input_str[low] == input_str[high]:
            return True
        else:
            return False
    else:
        if input_str[low] == input_str[high]:
            return is_palindrome( input_str, low+1, high-1 )
        else:
            return False

print(is_palindrome("racecar", 1, 3))

def binary_search(lst, low, high, val):
    if low > high:
        return None
    mid = (low+high)//2
    if lst[mid] == val:
        return mid
    else:
        if lst[mid] < val:
            return binary_search(lst, mid, high, val)
        else:
            return binary_search( lst, low, mid, val )

lst = [1,2,3,4,5,6,7]
print(binary_search(lst,0,len(lst)-1,3))

def split_parity(lst, low, high):
    if low == high:
        return lst
    else:
        if lst[low] % 2!=0:
            if lst[high] % 2 == 0:
                lst[low],lst[high] = lst[high],lst[low]
                return split_parity(lst, low+1, high-1)
            else:
                return split_parity( lst, low, high-1)

        else:
            return split_parity( lst, low+1, high)

lst=[4,-5,2,3,-1,-6,7,9,0]
print(split_parity(lst,0,len(lst)-1))

# a e i o u
# NYUT
def vc_count(word, low, high,vowels_lst = ['a','e','i','o','u','A','E','I','O','U']):
    if low > high:
        return (0,0)
    else:
        for i in vowels_lst:
            if word[low] == i:
                return (vc_count(word, low+1, high)[0]+1,vc_count(word, low+1, high)[1])
        return (vc_count(word, low+1, high)[0],vc_count(word, low+1, high)[1]+1)
word = 'NYUTandonEngineering'
print(vc_count(word, 0, len(word)-1) )

