class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

    @staticmethod
    def get_height(node):
        return node.height if node else 0

    def update_height(self):
        self.height = 1 + max(TreeNode.get_height(self.left), TreeNode.get_height(self.right))

    def balance_value(self):
        return TreeNode.get_height(self.right) - TreeNode.get_height(self.left)


class AVL_Tree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if not node:
            return TreeNode(data)

        if data < node.val:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return self.rebalance(node)

    def rebalance(self, node):
        node.update_height()

        balance = node.balance_value()

        # Left-heavy case
        if balance < -1:
            print("Right ", end="")
            if node.left and node.left.balance_value() > 0:
                node.left = self.rotate_left(node.left)  # Left-Right case
            return self.rotate_right(node)  # Left-Left case

        # Right-heavy case
        if balance > 1:
            print("Left ", end="")
            if node.right and node.right.balance_value() < 0:
                node.right = self.rotate_right(node.right)  # Right-Left case
            return self.rotate_left(node)  # Right-Right case
        return node

    def rotate_left(self, node):
        print("Left Rotation")
        new_root = node.right
        node.right = new_root.left
        new_root.left = node

        node.update_height()
        new_root.update_height()

        return new_root

    def rotate_right(self, node):
        print("Right Rotation")
        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        node.update_height()
        new_root.update_height()

        return new_root


def print_tree_90(node, level=0):
    if node:
        print_tree_90(node.right, level + 1)
        print('     ' * level, node)
        print_tree_90(node.left, level + 1)


my_tree = AVL_Tree()

print(" *** AVL Tree Insert Element ***")
data = list(map(int, input("Enter Input : ").split()))

root = None
for e in data:
    print(f"insert : {e}")
    root = my_tree.insert(root, e)
    print_tree_90(root)
    print("====================")
