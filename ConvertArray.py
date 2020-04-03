# def convertArray(dictionary):
#     a2 = [None] * len(dictionary)
#
#     index = 0
#     step = len(dictionary)//3
#     while index < step:
#         for i in range(0,len(dictionary),step):
#             a2[i] = dictionary[index]
#
#         index += 1
#     return a2
#
#
# print(convertArray(['a1','a2','a3','a4','b1','b2','b3','b4','c1','c2','c2','c4']))