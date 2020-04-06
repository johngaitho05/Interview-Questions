"""
This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields,it holds a
field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element to the end,
and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
"""

import _ctypes


class Node:
    def __init__(self, data):
        self.data = data
        self.npx = 0


class XORLinkedList:
    def __init__(self):
        self.start = None
        self.nodes = []

    def insert(self, x):
        temp = Node(x)
        if self.start is None:
            self.nodes.append(temp)
            self.start = temp
            return
        if self.start.npx == 0:
            self.start.npx = id(temp)
            temp.npx = id(self.start)
            return
        prev = self.start
        p = get_pointer(prev.npx)
        print(p)
        while p is not None:
            p = get_pointer(p.npx, prev=id(prev))
            prev = get_pointer(prev.npx)
        p = temp
        prev.npx ^= dereference_pointer(p)
        p.npx ^= dereference_pointer(prev)

    def display_list(self):
        if self.start is None:
            print("list is empty")
            return
        print(self.start.data)
        p = get_pointer(self.start.npx)
        print(type(p))
        while p is not None:
            print(p.data, end=' ')
            print()
            prev = p
            p = get_pointer(p.npx, prev=id(prev))


''' does not really work'''


def get_pointer(current, prev=0):
    print("Pointer is",id(current))
    if current == prev:
        return None
    xor = current ^ prev
    return _ctypes.PyObj_FromPtr(xor)


def dereference_pointer(node):
    return id(node)


if __name__ == '__main__':
    test_list = XORLinkedList()
    while True:
        print("Enter an action to perform\n")
        print("1.Insert")
        print("2.Display")
        choice = int(input(""))
        if choice == 1:
            to_insert = input("Enter the element to add: ")
            test_list.insert(to_insert)
        elif choice == 2:
            test_list.display_list()
