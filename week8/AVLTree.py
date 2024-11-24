import random as rd

class AVLNode :
    def __init__(self, data, left = None, right = None) :
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
        self.height = self.set_height()

    def __str__(self) :
        return str(self.data)
    
    def set_height(self) :
        a = self.get_height(self.left)
        b = self.get_height(self.right)
        self.height = 1 + max(a, b)
        return self.height

    def get_height(self, node) :
        return -1 if node is None else node.height
    
    def balance_value(self) :
        return self.get_height(self.left) - self.get_height(self.right)
    
class AVLTree :
    def __init__(self) -> None:
        self.root = None

    def add(self, data) :
        if self.root is None : self.root = AVLNode(data)
        else : self._add(self.root, data)

    def _add(self, root, data) :
        if data < root.data : 
            if root.left is None : root.left = AVLNode(data)
            else : self._add(root.left, data)
        else : 
            if root.right is None : root.right = AVLNode(data)
            else : self._add(root.right, data)

    def rebalanceS(self, x: AVLNode) :
        if x is None :
            return x
        
        balance = x.balance_value()
        if balance == -2 :
            if x.right.balance_value() == 1 :
                x.right = self.leftRotage(x.right)
                print("left rotage")
                print(self.root)
            x = self.rightRotage(x)
            print("right rotage")
            print(self.root)

        elif balance == 2 :
            if x.left.balance_value() == -1 :
                x.left = self.rightRotage(x.left)
                print("right rotage")
                print(self)
            x = self.leftRotage(x)
            print("left rotage")
            print(self)
        x.set_height()
        return x
    
    def leftRotage(self, x) :
        y = x.left
        x.left = y.right
        y.right = x
        x = y
        x.right.set_height()
        x.set_height()
        return x
    
    def rightRotage(self, x) :
        y = x.right
        x.right = y.left
        y.left = x
        x = y
        x.left.set_height()
        x.set_height()
        return x