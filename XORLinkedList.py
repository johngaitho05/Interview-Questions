# import _ctypes
# from secrets import token_bytes
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.npx = 0
#
#
# class XORLinkedList:
#     def __init__(self):
#         self.start = None
#         self.nodes = []
#
#     def insert(self, x):
#         temp = Node(x)
#         if self.start is None:
#             self.nodes.append(temp)
#             self.start = temp
#             return
#         if self.start.npx == 0:
#             self.start.npx =
#             temp.npx = id(self.start)
#             return
#         prev = self.start
#         p = get_pointer(prev.npx)
#         print(p)
#         # while p is not None:
#         #     p = get_pointer(p.npx, prev=id(prev))
#         #     prev = get_pointer(prev.npx)
#         # p = temp
#         # prev.npx ^= dereference_pointer(p)
#         # p.npx ^= dereference_pointer(prev)
#
#     def display_list(self):
#         if self.start is None:
#             print("list is empty")
#             return
#         print(self.start.data)
#         p = get_pointer(self.start.npx)
#         print(type(p))
#         while p is not None:
#             print(p.data, end=' ')
#             print()
#             prev = p
#             p = get_pointer(p.npx, prev=id(prev))
#
#
# def get_pointer(current, prev=0):
#     if current == prev:
#         return None
#     xor = current ^ prev
#     return _ctypes.PyObj_FromPtr(xor)
#
#
# def dereference_pointer(node):
#         return id(node)
#
#
# if __name__ == '__main__':
#     test_list = XORLinkedList()
#     while True:
#         print("Enter an action to perform\n")
#         print("1.Insert")
#         print("2.Display")
#         choice = int(input(""))
#         if choice == 1:
#             to_insert = input("Enter the element to add: ")
#             test_list.insert(to_insert)
#         elif choice == 2:
#             test_list.display_list()
#
