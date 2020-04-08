def powerOf2(n):
    if n < 0:
        raise ValueError("Invalid value on n")
    if n == 1:
        return 0
    power = 1  # initialize power as one
    numbers_list = []
    while 2 ** power <= n:  # loop terminates when the next power of 2 is bigger than n
        numbers_list.append(2 ** power)  # print number
        power += 1  # increment power
    return numbers_list


print(powerOf2(250))
