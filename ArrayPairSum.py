def findPair(a, k):
    seen = set()
    pairs = set()
    for i in range(len(a)):
        other_num = k - a[i]
        if other_num in seen:
            pairs.append((other_num, a[i]))
        else:
            pairs.add((min(a[i], other_num), max(a[i], other_num)))
    print('\n'.join(map(str, list(pairs))))


findPair([2, 5, 5, 3, 7, 4, 6], 9)