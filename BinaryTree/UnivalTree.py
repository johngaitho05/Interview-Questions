'''
This problem was asked by Google.

A unival tree (which stands for "universal value") is dictionary tree where all nodes under it have the same value.

Given the root to dictionary binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

from BinaryTree.LinkedBinaryTree import LInkedBinaryTree, Node


def num_universal_trees(root):
    if root is None:
        return 0
    x = root.lchild
    y = root.rchild
    if x == y is None:
        return 1 + num_universal_trees(root.lchild) + num_universal_trees(root.rchild)
    if x is not None and y is not None:
        if x.info == y.info:
            return 1 + num_universal_trees(root.lchild) + num_universal_trees(root.rchild)
        return num_universal_trees(root.lchild) + num_universal_trees(root.rchild)
    return num_universal_trees(root.lchild) + num_universal_trees(root.rchild)


bt = LInkedBinaryTree()

bt.root = Node(0)
bt.root.lchild = Node(1)
bt.root.rchild = Node(0)
bt.root.rchild.lchild = Node(1)
bt.root.rchild.rchild = Node(0)
bt.root.rchild.lchild.lchild = Node(1)
bt.root.rchild.lchild.rchild = Node(1)
bt.display()
print("No of universal subtrees = ", num_universal_trees(bt.root))
