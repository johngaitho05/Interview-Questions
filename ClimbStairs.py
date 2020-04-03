def num_ways(n, x):
    if n < 0:
        raise ValueError("Invalid value of n")
    if n == 0:
        return 1
    nums = [None] * (n+1)
    nums[0] = 1
    for i in range(1, n+1):
        total = 0
        for j in x:
            if i-j >= 0:
                total += nums[i-j]
        nums[i] = total
    print(nums)
    return nums[n]


n = 8
x = [1,2,5]

print(num_ways(n,x))



