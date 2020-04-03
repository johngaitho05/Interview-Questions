'''
This problem was asked by Facebook.

Given the mapping dictionary = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def helper(data, k, memo):
    if k == 0:
        return 1
    s = len(data) - k
    if data[s] == '0':
        return 0
    if memo[k] is not None:
        return memo[k]
    result = helper(data, k-1, memo)
    if k >= 2 and int(data[s:s+2]) <= 26:
        result += helper(data, k-2, memo)
    memo[k] = result
    return result


def num_ways(data):
    memo = [None] * (len(data)+1)
    return helper(data,len(data), memo)


print(num_ways("14211"))




def num_ways2(s):
    l = len(s)
    if l == 0:
        return 1
    if l == 1:
        return 1
    if l == 2:
        if int(s) <= 26:
            return 2
        else:
            return 1
    temp = [None]* l
    temp[-1]= 1
    temp[l-2] = num_ways2(s[l-2:])
    for i in range(l-3, -1, -1):
        if int(s[i]) <= 2:
            temp[i] = int(temp[i+1]) + int(temp[i+2])
        else:
            temp[i] = int(temp[i + 1])
    print(temp)
    return temp[0]


print(num_ways2("11111"))







