from BinaryTree.BinarySearchTree import BinarySearchTree
from Sorting.Sorting import bubble_sort


# naive solution
def isBST(tree):
    return check_left(tree.root.lchild,tree.root.info) is True and check_right(tree.root.rchild,tree.root.info) is True


def check_left(node, max):
    if node is None:
        return True
    if node.lchild is None and node.rchild is None:
        if node.info < max:
            return True
        else:
            return False
    if node.rchild is None:
        if node.lchild.info <= node.info and node.lchild.info <= max:
            return check_left(node.lchild,max)
        else:
            return False
    elif node.lchild is None:
        if node.info <= node.rchild.info <= max:
            return check_left(node.rchild,max)
        else:
            return False
    else:
        if check_left(node.lchild,max):
            return check_left(node.rchild, max)
        else:
            return False


def check_right(node,min):
    if node is None:
        return True
    if node.lchild is None and node.rchild is None:
        if node.info >= min:
            return True
        else:
            return False
    elif node.lchild is None:
        if node.info <= node.rchild.info >= min:
            return check_right(node.rchild,min)
        else:
            return False
    else:
        if check_right(node.lchild,min):
            return check_right(node.rchild, min)
        else:
            return False


# optimal solution
def isBST2(tree):
    if tree.inorder() == bubble_sort(tree.inorder()):
        return True
    else:
        return False


# test cases
btree1 = BinarySearchTree([140,100,45,70,70,45,120,75])
print(isBST(btree1))
print(isBST2(btree1))






