class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
            
    def _insert(self, root, data) :
        if data < root.data :
            if root.left == None :
                root.left = Node(data)
            else :
                self._insert(root.left, data)
        else :
            if root.right == None :
                root.right = Node(data)
            else :
                self._insert(root.right, data)
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
            
    def reverseTree(self, node):
        if node != None :
            node.left, node.right = node.right, node.left
            self.reverseTree(node.left)
            self.reverseTree(node.right)
        

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)

print("Before:")
T.printTree(T.root)

T.reverseTree(T.root)

print("After:")
T.printTree(T.root)