# Author: John YK

def largest_noncontagious_sum(a):
    l = len(a)
    if l == 0:
        return 0
    if l == 1:
        return a[0]
    if l == 2:
        return max(a)
    if a[l-1] > a[l-2]:
        a[l-2] = a[l-1]
    for i in range(l-3, -1, -1):
        a[i] = max(a[i],a[i]+max(a[i+2:]))
    return max(a)

# tests
print(largest_noncontagious_sum([2,4,6,2,5]))
print(largest_noncontagious_sum([5,1,1,5]))




























def max_sum(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return max(a)
    for i in range(len(a)-2):
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






