"""Linear search"""
# We are given an array:
# myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
# Write a function that returns to us the index of the desired value using a linear search from the array.
# If the value you are looking for does not exist in the array, return -1 or No.

def LinearSearch(data,list):
    for n in range(len(list)):
        if list[n]==data:
            return n
    return None

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]    
print(LinearSearch(8, myList))

"""BINARY SEARCH"""
# There is an A list of N elements.
# The value we are looking for is T.
# And we need a T index

# ALGORITHMS
# 1.We set the lower limit to L = 0 and the upper limit to H = N-1
# 2.If L> H, do not search
# 3.We find the middle of the list: m (L + H) / 2
# 4.If A index == T returns A index and the program stops
# 5.If the index A is> T, we form H = m-1 and return to step 2
# 6.If the index A is <T, we do L = m + 1 and return to step 2

def BinarySearch(list,data):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        guess = list[mid]
        if guess==data:
            return mid
        elif guess>data:
            high = mid - 1
        else:
            low = mid + 1
    return None
            
myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
print(BinarySearch(myList, 7))  