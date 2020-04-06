def largestContinuousSum(arr):
    if len(arr) == 0:
        return
    maxSum = currentSum = arr[0]
    for num in arr[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(currentSum, maxSum)
    return maxSum


print(largestContinuousSum([3, -5, 2, -4, 6, -9, 9, -10]))
