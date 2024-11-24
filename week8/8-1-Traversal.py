class AVLTree:
    
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
            self.height = 1  
        
        def __str__(self):
            return str(self.data)
        
        def updateHeight(self):
            self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
        
        @staticmethod
        def getHeight(node):
            return node.height if node else 0
        
        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, node, data):
        if node is None:
            return self.AVLNode(data)
        if int(data) < int(node.data):
            node.left = self._add(node.left, data)
        else:
            node.right = self._add(node.right, data)
        return self.rebalance(node)

    def rebalance(self, node):
        if node is None:
            return node
        
        node.updateHeight()
        balance = node.balanceValue()

        if balance < -1:  
            if node.left.balanceValue() > 0:  
                node.left = self.rotateLeftChild(node.left)
            node = self.rotateRightChild(node)  

        elif balance > 1: 
            if node.right.balanceValue() < 0:  
                node.right = self.rotateRightChild(node.right)
            node = self.rotateLeftChild(node)  

        return node

    def rotateLeftChild(self, node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        node.updateHeight()
        temp.updateHeight()
        return temp

    def rotateRightChild(self, node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        node.updateHeight()
        temp.updateHeight()
        return temp

    def postOrder(self):
        print("AVLTree post-order : ", end="")
        self._postOrder(self.root)
        print()

    def _postOrder(self, node):
        if node:
            self._postOrder(node.left)
            self._postOrder(node.right)
            print(node, end=" ")

    def printTree(self):
        self._printTree(self.root)
        print()

    def _printTree(self, node, level=0):
        if node:
            self._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self._printTree(node.left, level + 1)

avl_tree = AVLTree()
inp = input('Enter Input : ').split(',')

for i in inp:
    if i.startswith("AD"):
        avl_tree.add(i[3:])
    elif i.startswith("PR"):
        avl_tree.printTree()
    elif i.startswith("PO"):
        avl_tree.postOrder()
