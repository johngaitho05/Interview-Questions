# first method (using XOR)
def findMissingNumber(array1, array2):
    result=0
    for num in array1+array2:
        result^=num
    return result

#  second method (using python set)
def findMissingNumber2(array1,array2):
    missing = set(array1) - set(array2)
    return missing.pop()


arr1 = [3,10,7,6,12,1]
arr2 = [10,3,1,6,12]

print(findMissingNumber(arr1,arr2))
print(findMissingNumber2(arr1,arr2))

