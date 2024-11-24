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

    def deleteNode(self, key) :
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, node, key) :
        if key < node.data :
            node.left = self._deleteNode(node.left, key)
        elif key > node.data :
            node.right = self._deleteNode(node.right, key)
        else :

            # case 1: delete leaf node
            if not node.left and not node.right : return None

            #case 2: has one children
            elif not node.left : return node.right
            elif not node.right : return node.left

            #case 3: Node has two childen
            else :
                # find in-order successor
                temp = self._minValueNode(node.right)
                node.data = temp.data
                node.right = self._deleteNode(node.right, temp.data)
        return node
    
    def _minValueNode(self, node) :
        curr = node
        while curr.left :
            curr = curr.left

        return curr


    def get_node_height(self, node) :
        if not node : return 0
        return 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

inp = list(map(int, input("num input: ").split(" ")))
bst = BST()
for i in inp :
    bst.add(i)

bst.printTree(bst.root)
print("=======================")
bst.deleteNode(70)
bst.printTree(bst.root)