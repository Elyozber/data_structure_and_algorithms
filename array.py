def rotate(array,d):
    n = len(array)
    d = d%n
    arr = array[:d]
    for s in range(d):
        del array[0]
        
    for a in arr:
        array.append(a)
        
    return array

array = [1,2,3,4,5,6,7,8]
d = 4
print(rotate(array,d))


def array1(array,d):
    arr = array[:]
    for s in range(d):
        for a in arr:
            array.append(a)
    return array

array = [1,2,3]
d = 4
print(array1(array,d))


def array3(nums1,nums2):
    nums3 = []
    for num in nums1:
        for numm in nums2:
            if num==numm:
                nums3.append(num)
    print(nums1)
    print(nums2)
    return nums3


nums1 = [1,2,3,4,5]
nums2 = [2,5,7,8,9,11]
print(array3(nums1, nums2))


def partitionDisjoint(array,d):
    n = len(array)
    d = d%n
    left = array[:d]
    right = array[d:]
    print(right)
    return left   

array = [32,324,435,546,567,78,58,98,789,879,678]
d = 3
print(partitionDisjoint(array, d))