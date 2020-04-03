from Data_Structures.Queue import ArrayQueue


class Node:
    def __init__(self,name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None


# uses queue => layer by layer traversal
class BreadthFirstSearch(object):

    def bfs(self, startNode):
        queue = ArrayQueue()
        queue.enqueue(startNode)
        startNode.visited = True

        while not queue.is_empty():
            actualNode = queue.dequeue()
            print("%s" % actualNode.name)
            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    queue.enqueue(n)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacencyList.append(node2)
node1.adjacencyList.append(node3)
node2.adjacencyList.append(node4)
node4.adjacencyList.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)














