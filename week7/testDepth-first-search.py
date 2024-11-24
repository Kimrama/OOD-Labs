class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) :
        return str(self.data)
    
class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) :
        if self.root == None : self.root = Node(data)
        else :
            self._insert(self.root, data)

    def _insert(self, root, data) :
        if data < root.data :
            if root.left == None : root.left = Node(data)
            else : self._insert(root.left, data)
        else :
            if root.right == None : root.right = Node(data)
            else : self._insert(root.right, data)

    def print_DFS(self, root) :
        if root == None : return
        print(root.data, end="->")
        self.print_DFS(root.left)
        self.print_DFS(root.right)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)

print("tree:")
T.printTree(T.root)

T.print_DFS(T.root)