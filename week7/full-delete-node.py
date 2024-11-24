class Node:
    def __init__(self, data) :
        self.left = None
        self.right = None
        self.data = data
    def __str__(self) : return str(self.data)


class BST :
    def __init__(self) -> None:
        self.root = None

    def add(self, data) :
        if self.root is None : self.root = Node(data)
        else : self._add(self.root, data)

    def _add(self, root, data) :
        if data < root.data :
            if root.left is None : root.left = Node(data)
            else : self._add(root.left, data)
        else :
            if root.right is None : root.right = Node(data)
            else : self._add(root.right, data)
        
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def delete(self, key):
        self.root = self._deleteNode(self.root, key)

    def _deleteNode(self, root, data):
        if root is None :
            return root
        
        if data < root.data : 
            root.left = self._deleteNode(root.left, data)
        elif data > root.data :
            root.right = self._deleteNode(root.right, data)

        else :
            if root.left is None : 
                return root.right
            elif root.right is None : 
                return root.left


            temp = self.get_min(root.right)

            root.data = temp.data

            root.right = self._deleteNode(root.right, temp.data)
        return root


    def get_min(self, root) :
        curr = root

        while curr.left != None : curr = curr.left

        return curr

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.add(i)

print("tree:")
T.printTree(T.root)

T.delete(7)
print("tree:")
T.printTree(T.root)