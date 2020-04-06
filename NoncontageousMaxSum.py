"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the
largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick
2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_noncontagious_sum(a):
    length = len(a)
    if length == 0:
        return 0
    if length == 1:
        return a[0]
    if length == 2:
        return max(a)
    if a[length - 1] > a[length - 2]:
        a[length - 2] = a[length - 1]
    for i in range(length - 3, -1, -1):
        a[i] = max(a[i], a[i] + max(a[i + 2:]))
    return max(a)


# tests
print(largest_noncontagious_sum([2, 4, 6, 2, 5]))
print(largest_noncontagious_sum([5, 1, 1, 5]))


def max_sum(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return max(a)
    for i in range(len(a) - 2):
        value = find_max(a, i)
        if value == a[i]:
            return max(a)
        a[i] = value
    return max(a)


def find_max(a, index):
    initial = max_val = a[index]
    i = index + 2
    while i < len(a):
        new_max = a[i] + initial
        if new_max > max_val:
            max_val = new_max
        if len(a) > i + 2:
            to_add = a[i]
            for j in range(i + 2, len(a), 2):
                if a[j] + to_add > to_add:
                    to_add += a[j]
            new_max = to_add + initial
            if new_max > max_val:
                max_val = new_max
        i += 1

    return max_val
