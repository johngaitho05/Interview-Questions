def minimum_cost(M):
    cols = len(M[0])
    if cols == 0:
        print('invalid Matrix')
        return
    if cols == 1:
        return min(M[0])
    for i in range(1, len(M)):
        if len(M[i]) != cols:
            print('invalid Matrix')
            return
    rows = len(M)
    memo = [[None]*cols]*rows
    n = rows-1
    for k in range(cols):
        M[n][k] = helper2(M, n, k, memo)
    return min(M[n])


def helper2(M, n, k, memo):
    if n == 0:
        return M[n][k]
    if memo[n][k] is not None:
        return memo[n][k]
    min_val = None
    for i in range(len(M[0])):
        if i == k:
            pass
        elif min_val is None or min_val > helper2(M, n - 1, i, memo):
            min_val = helper2(M, n - 1, i, memo)
    result = min_val + M[n][k]
    memo[n][k] = result
    print(memo)
    return result


matrix = [
    [6, 3, 7],
    [9, 4, 12],
    [3, 8, 7]
]

print(minimum_cost(matrix))


# def helper(M, index, cols):
#     while index < len(M):
#         sub = M[index]
#         for i in range(cols):
#             temp = None
#             for j in range(cols):
#                 if j == i:
#                     continue
#                 if temp is None or M[index - 1][j] < temp:
#                     temp = M[index - 1][j]
#             sub[i] += temp
#         index += 1
#     print(M)
#     return min(M[len(M) - 1])
