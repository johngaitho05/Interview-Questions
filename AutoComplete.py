
from Trees.TernarySearchTree import TernarySearchTree


def auto_complete(sub_string, dictionary):
    tst = TernarySearchTree(dictionary)
    return tst.find_matches(sub_string)


# tests
d = ['apple', 'deal', 'dog', 'debt', 'deer']
s = 'de'
print(auto_complete(s, d))











