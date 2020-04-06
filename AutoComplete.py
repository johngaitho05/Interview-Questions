"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

from Data_Structures.Trees.TernarySearchTree import TernarySearchTree


def auto_complete(sub_string, dictionary):
    tst = TernarySearchTree(dictionary)
    return tst.find_matches(sub_string)


# tests
d = ['apple', 'deal', 'dog', 'debt', 'deer']
s = 'de'
print(auto_complete(s, d))











