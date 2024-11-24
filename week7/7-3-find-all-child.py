class Node:
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __str__(self) : return str(self.data)


class BST:
    def __init__(self) :
        self.root = None
    
    def add(self, data) :
        if self.root == None : self.root = Node(data)
        else : self._add(self.root, data)

    def _add(self, root, data) :
        if data < root.data :
            if root.left == None : root.left = Node(data)
            else : self._add(root.left, data)
        else :
            if root.right == None : root.right = Node(data)
            else : self._add(root.right, data)
            
    def bfs(self, target) :
        queue = [self.root]
        while (len(queue) != 0) :
            node = queue.pop(0)
            if node.data == target : return node
            if node.left : queue.append(node.left)
            if node.right : queue.append(node.right)
        return -1


    def printTree(self, node, level = 0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level + " " + str(node))
            self.printTree(node.left, level + 1)

    def get_decendent(self, parent) :
        root = self.bfs(parent)
        result = []
        self.get_decendent_dfs(result, root)
        return result

    def get_decendent_dfs(self, result,  root) :
        if root == None : return
        result.append(root.data)
        self.get_decendent_dfs(result, root.left)
        self.get_decendent_dfs(result, root.right)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.add(i)

print("Before:")
T.printTree(T.root)
print(T.get_decendent(8))