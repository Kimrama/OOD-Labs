class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # New attribute for AVL tree node height

    def __str__(self) -> str:
        return str(self.data)

class AVLTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, node, data):
        if node is None:
            return TreeNode(data)

        if data < node.data:
            node.left = self._add(node.left, data)
        else:
            node.right = self._add(node.right, data)

        # Update height using the new set_height method
        self.set_height(node)

        # Rebalance the node after insertion
        return self.rebalance(node)

    def set_height(self, node):
        """
        Updates the height of the node based on the height of its children.
        """
        if node is not None:
            node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

    def rebalance(self, node):
        balance = self.get_balance(node)

        # LL Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)

        # LR Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # RR Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)

        # RL Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        # Update heights after rotation
        self.set_height(z)
        self.set_height(y)

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        # Update heights after rotation
        self.set_height(z)
        self.set_height(y)

        return y

    def get_node_height(self, node):
        """
        Returns the height of the node.
        """
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """
        Returns the balance factor of the node.
        """
        if not node:
            return 0
        return self.get_node_height(node.left) - self.get_node_height(node.right)

    def deleteNode(self, node, key):
        if not node:
            return node

        if key < node.data:
            node.left = self.deleteNode(node.left, key)
        elif key > node.data:
            node.right = self.deleteNode(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self.get_min_value_node(node.right)
            node.data = temp.data
            node.right = self.deleteNode(node.right, temp.data)

        if not node:
            return node

        # Update height using the new set_height method
        self.set_height(node)

        # Rebalance the node after deletion
        return self.rebalance(node)

    def get_min_value_node(self, node):
        """
        Returns the node with the smallest value in the subtree.
        """
        if node is None or node.left is None:
            return node
        return self.get_min_value_node(node.left)

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + " " + str(node))
            self.printTree(node.left, level + 1)

# Test the AVL Tree
inp = list(map(int, input("num input: ").split(" ")))
avl = AVLTree()
for i in inp:
    avl.add(i)

avl.printTree(avl.root)
