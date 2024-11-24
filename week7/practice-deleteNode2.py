class TreeNode :
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return str(self.data)
    
class BST :
    def __init__(self) :
        self.root = None

    def add(self, data) :
        if self.root is None : self.root = TreeNode(data)
        else : self._add(self.root, data)

    def _add(self, node, data) :
        if data < node.data : 
            if node.left is None : node.left = TreeNode(data)
            else : self._add(node.left, data)
        else  : 
            if node.right is None : node.right = TreeNode(data)
            else : self._add(node.right, data)

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + " " + str(node))
            self.printTree(node.left, level + 1)

    def deleteNode(self, node,  key) :
        if not node : return None

        if node.data == key :

            if not node.left and not node.right : return None
            if not node.left and node.right : return node.right
            if not node.right and node.left : return node.left


            pt = node.right
            while pt.left : pt = pt.left

            node.data = pt.data
            node.right = self.deleteNode(node.right, node.data)

        elif key < node.data :
            node.left = self.deleteNode(node.left, key)
        else :
            node.right = self.deleteNode(node.right, key)

        return node

    def get_node_height(self, node) :
        if not node : return 0
        return 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

inp = list(map(int, input("num input: ").split(" ")))
bst = BST()
for i in inp :
    bst.add(i)

bst.printTree(bst.root)
print("=======================")
bst.deleteNode(bst.root, 5)
bst.printTree(bst.root)