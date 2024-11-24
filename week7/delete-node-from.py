class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def deleteNode(root, key):
    # Base case: if the tree is empty
    if root is None:
        return root

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children:
        # Get the inorder successor (smallest in the right subtree)
        temp = findMinValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root

def findMinValueNode(node):
    current = node

    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current

# Helper function to do inorder traversal
def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.val, end=" ")
        inorderTraversal(root.right)

# Example usage
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Inorder traversal before deletion:")
inorderTraversal(root)

key = 70
root = deleteNode(root, key)

print("\nInorder traversal after deletion:")
inorderTraversal(root)
