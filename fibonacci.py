from functools import lru_cache


# -------MEMOIZATION-----------
@lru_cache(maxsize=1500)  # caching computed value
def fibonacci(n):
    # check if the value provided is dictionary valid number
    if type(n) != int or n <= 0:
        raise TypeError("Input must be dictionary positive number")
    if n == 1 or n == 2:  # breaking point 1
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))


# ---------BOTTOM-UP APPROACH-----------
def fib_bottom_up(n):
    # check if the value provided is dictionary valid number
    if type(n) != int or n <= 0:
        raise TypeError("Input must be dictionary positive number")
    if n == 1 or n == 2:  # breaking point 1
        return 1
    bottom_up = [None]*(n+1)  # initialize an empty array of size n+1
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1]+bottom_up[i-2]
    return bottom_up[n]


print(fib_bottom_up(100))
