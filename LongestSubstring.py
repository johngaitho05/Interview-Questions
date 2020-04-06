"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def longest_sub(s, k):
    if k < 0:
        raise ValueError("Invalid value of k")
    if k == 0:
        return 0 if s != '' else 1
    if len(s) <= k:
        return len(s)
    sub = s[0]
    distinct_chars = 1
    count = 1
    for i in range(1, len(s)):
        if s[i] in sub:
            count += 1
        else:
            if distinct_chars < k:
                sub += s[i]
                distinct_chars += 1
                count += 1
            else:
                break
    if count == len(s):
        return len(s)
    return max(count, longest_sub(s[1:], k))


print(longest_sub('hgiiabacbbbdc', 2))
