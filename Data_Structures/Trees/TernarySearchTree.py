class Node:
    def __init__(self, character):
        self.character = character
        self.leftNode = None
        self.middleNode = None
        self.rightNode = None
        self.value = None


class TernarySearchTree:
    def __init__(self, initial_elements=None):
        self.rootNode = None
        if initial_elements is not None:
            for element in initial_elements:
                self.put(element)

    def put(self, key, value=0):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)

    def putItem(self, node, key, value, index):
        c = key[index]

        if node is None:
            node = Node(c)

        if c < node.character:
            node.leftNode = self.putItem(node.leftNode, key, value, index)
        elif c > node.character:
            node.rightNode = self.putItem(node.rightNode, key, value, index)
        elif index < len(key) - 1:
            node.middleNode = self.putItem(node.middleNode, key, value, index + 1)
        else:
            node.value = value
        return node

    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)
        if node is None:
            return
        return node

    def getItem(self, node, key, index):
        if node is None:
            return
        c = key[index]
        if c < node.character:
            return self.getItem(node.leftNode, key, index)
        elif c > node.character:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index + 1)
        else:
            return node

    def find_matches(self, s):
        node = self.get(s)
        if node is None:
            return
        matches = [s + sub for sub in self.traverse(node.middleNode)]
        if node.value is not None:
            matches.append(s)
        return matches

    def traverse(self, node):
        if node is None:
            return []
        if node.leftNode is None and node.middleNode is None and node.rightNode is None:
            return [node.character]
        result = [node.character + s for s in self.traverse(node.middleNode)]
        if not result:
            result = [node.character]
        result.extend(self.traverse(node.leftNode) + self.traverse(node.rightNode))
        return result


if __name__ == '__main__':
    t = TernarySearchTree()
    t.put('hello', 100)
    t.put('world', 200)

    print(t.get('world').value)
