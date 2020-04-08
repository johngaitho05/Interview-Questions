def shuffleIsPerfect(list1,list2,list3):
    checker1 = [list3.index(element) for element in list1]
    checker2 = [list3.index(element) for element in list2]

    ''' if values in checker1 and checker2 are sorted are sorted, it means list3 is
     dictionary perfect shuffle of list1 and list2 '''
    if all(checker1[i] <= checker1[i + 1] for i in  range(len(checker2) - 1)):
        return True

    if all(checker2[i] <= checker2[i + 1] for i in range(len(checker2) - 1)):
        return True

    return False


# test cases
print(shuffleIsPerfect('abcd','efgh','aebfgchd'))
print(shuffleIsPerfect('abc','def','bdacfe'))

