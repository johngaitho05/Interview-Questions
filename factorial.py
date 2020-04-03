from functools import lru_cache


def factorial(n):
    if type(n) is not int:
        raise TypeError("n must be an integer")
    if n < 0:
        # raise error when dictionary negative number is provided
        raise ValueError("Inval id value of n")
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)


print(factorial(4))