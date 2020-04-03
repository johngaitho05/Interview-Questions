
"""
Give an array containing n+1 integers where each integer is between 1 and n(inclusive),
Prove that at least one duplicate number must exist.
Assume that there is only one duplicate number but it could be repeated more than once
"""


def findDuplicate(a):
    for num in a:
        if a[abs(num)] < 0:
            return abs(num)
        else:
            a[abs(num)] *= -1
    return


def findDuplicate2(a):
    t = a[0]
    h = a[0]
    while True:
        t = a[t]
        h = a[a[h]]
        if t == h:
            break

    ptr1 = a[0]
    ptr2 = t
    while ptr1 != ptr2:
        ptr1 = a[ptr1]
        ptr2 = a[ptr2]

    return ptr1

 
print(findDuplicate([2,4,1,3,2]))
print(findDuplicate2([2,4,1,3,2]))


















