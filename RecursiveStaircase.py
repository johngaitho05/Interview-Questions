"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of
positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


def num_ways(n, x):
    if n < 0:
        raise ValueError("Invalid value of n")
    if n == 0:
        return 1
    nums = [None] * (n + 1)
    nums[0] = 1
    for i in range(1, n + 1):
        total = 0
        for j in x:
            if i - j >= 0:
                total += nums[i - j]
        nums[i] = total
    print(nums)
    return nums[n]


print(num_ways(8, [1, 3, 5]))
