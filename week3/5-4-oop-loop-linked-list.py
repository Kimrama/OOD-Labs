class Node :
    def __init__(self, data, next=None) :
        if next == None : self.next = None
        else : self.next = next
        self.data = data

    def __str__(self) :
        return f"{self.data}"
    

class List :
    def __init__(self) :
        self.head = None
        self.shape = 0

    def append_node(self, data) :
        if self.head == None : 
            self.head = Node(data)
            self.shape += 1
            self.print_list()
        else :
            n = self.head
            while n.next != None : n = n.next
            n.next = Node(data)
            self.shape += 1
            self.print_list()
    
    def print_list(self) :
        if self.head == None : return
        else :
            n = self.head
            seq_node = []
            while n != None :
                if n in seq_node : 
                    print("Found Loop")
                    break
                seq_node.append(n)
                n = n.next
            print("->".join(seq_node))

    def search_node_by_index(self, index) :
        if self.head == None : return
        else :
            n = self.head
            run = 0
            while run < index :
                n = n.next
                run += 1
                if run > self.shape : return None
            return n
    
    

li = List()

data = ["1","2","3","4"]
for (i) in data : li.append_node(i)

# li.print_list()
# print(li.search_node_by_index(0))