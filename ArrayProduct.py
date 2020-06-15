"""
Given an array of integers, return dictionary new array such that each element at index i of the new array is
the product of all the numbers in the original array except the one at i.

For example, if our s was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our s was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


# solution 1 (using division)
def arrayProducts(a):
    new_array = [None]*len(a)
    prod = get_product(a)
    for i in range(len(a)):
        new_array[i] = prod//a[i]
    return new_array


# solution 2: what if you can't use division?

def arrayProducts2(a):
    new_array = [None]*len(a)
    original = a
    for i in range(len(a)):
        new_array[i] = get_product(a[0:i]+a[i+1:])
        a = original
    return new_array


def get_product(a):
    prod = 1
    for i in range(len(a)):
        prod *= a[i]
    return prod


print(arrayProducts([1, 2, 3, 4, 5]))
print(arrayProducts2([1, 2, 3, 4, 5]))


