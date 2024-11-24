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

    def print_tree_pyramid(self):
        if not self.root:
            return
        
        queue = [self.root]
        tree_height = self.get_node_height(self.root)
        max_width = 2 ** tree_height - 1  
        
        current_level = 0
        while queue:
            current_level_size = len(queue)
            indent = max_width // (2 ** current_level + 1)
            
            level_output = " " * indent
            next_level_queue = []
            
            for i in range(current_level_size):
                node = queue[i]
                if node:
                    level_output += str(node.data)
                    next_level_queue.extend([node.left, node.right])
                else:
                    level_output += " "
                    next_level_queue.extend([None, None])
                
                if i < current_level_size - 1:
                    level_output += " " * (2 * indent - 1)
            
            print(level_output)
            queue = next_level_queue
            current_level += 1

            if all(node is None for node in queue):
                break

    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + " " + str(node))
            self.printTree(node.left, level + 1)

    def get_node_height(self, node) :
        if not node : return 0
        return 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

inp = list(map(int, input("num input: ").split(" ")))
bst = BST()
for i in inp :
    bst.add(i)

bst.print_tree_pyramid()