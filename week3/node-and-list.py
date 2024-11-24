class Node :
    def __init__(self, data, next = None) :
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next


    def __str__(self) -> str:
        return f"{self.data}"
    
class List :
    def __init__(self, head=None) :

        if head is None :
            self.head = self.tail = None
            self.shape = 0
        else :
            self.head = head
            t = self.head
            self.size = 1

            while t.next != None :
                t = t.next
                self.shape += 1

            self.tail = t

    def append(self, data) :
        p = Node(data)
        if self.head == None : self.head = p
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = p
        self.shape += 1

    def add_head(self, data) :
        p = Node(data)
        p.next = self.head
        self.head = p
        self.shape += 1

    def pop_head(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.shape -= 1
        return p
    
    