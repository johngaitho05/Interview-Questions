def smallestMissingPosInteger(a):
    if len(a) == 0:  # return 1 if the list is empty
        if a[0] == 1:  # the list has 1 element
            return 2
        return 1
    j = 0
    if max(a) < 1:  # all values are negatives
        return 1
    for i in range(0,len(a)):  # move all negatives to the left side
        if a[i]<0:
            a[i],a[j] = a[j],a[i]
            j+=1

    a = [abs(x) for x in a]  # make all values positive
    for i in range(j,len(a)):
        if abs(a[i]) <= len(a):
            if a[abs(a[i])-1]>0:
                a[abs(a[i])-1] = a[abs(a[i])-1] * -1  # modify the value of the element at the given index to negative
    # iterate the array and check the first positive element and return its index+1
    for i in range(0,len(a)):
        if a[i]>0:
            return i+1
    return len(a)+1


# tests
a1 = [-1,2,-3,5,11,-4]
a2 = [3, 4, -1, 1]
a3 = [2]
a4 = [1,4,5,2,9,6,7]
a5 = [-1,-4,-5,-2,-9,-6,-7]
a6 = [1,2,3,4,5,6]
a7 = [37,45,19,60]
print(smallestMissingPosInteger(a1))
print(smallestMissingPosInteger(a2))
print(smallestMissingPosInteger(a3))
print(smallestMissingPosInteger(a4))
print(smallestMissingPosInteger(a5))
print(smallestMissingPosInteger(a6))
print(smallestMissingPosInteger(a7))









