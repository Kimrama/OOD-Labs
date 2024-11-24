class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self):
        self.root = None

    # Method to insert nodes into the tree (Binary Search Tree insertion)
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert(current_node.right, key)
        else:
            # If key is equal to current node value, no insertion (BST rule)
            pass

    # Method to print the tree in pyramid form
    def print_tree_pyramid(self):
        if not self.root:
            return
        
        # Initialize a queue for level order traversal
        queue = [self.root]
        tree_height = self._get_tree_height(self.root)
        max_width = 2 ** tree_height - 1  # Maximum width of the tree's bottom level
        
        current_level = 0
        while queue:
            current_level_size = len(queue)
            # Calculate the appropriate spacing for the current level
            indent = max_width // (2 ** current_level + 1)
            
            # Print nodes at the current level
            level_output = " " * indent
            next_level_queue = []
            
            for i in range(current_level_size):
                node = queue[i]
                if node:
                    level_output += str(node.val)
                    next_level_queue.extend([node.left, node.right])
                else:
                    level_output += " "
                    next_level_queue.extend([None, None])
                
                if i < current_level_size - 1:
                    # Add space between nodes
                    level_output += " " * (2 * indent - 1)
            
            print(level_output)
            queue = next_level_queue
            current_level += 1

            # Break if the next level is entirely None
            if all(node is None for node in queue):
                break

    # Method to calculate the height of the tree
    def _get_tree_height(self, node):
        if not node:
            return 0
        return 1 + max(self._get_tree_height(node.left), self._get_tree_height(node.right))

# Example usage:
tree = Tree()

# Insert nodes into the tree
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

# Print the tree in pyramid form
print("Tree in pyramid form:")
tree.print_tree_pyramid()
