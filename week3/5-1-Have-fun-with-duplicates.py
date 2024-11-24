class Node :
    def __init__(self, data, next=None, front=None) :
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next
        if front is None :
            self.front = None
        else :
            self.front = front

    def __str__(self) :
        return f"{self.data}"
        

class List :
    def __init__(self, head=None) :
        if head is None :
            self.head = None
        else :
            self.head = head
        self.dup_list = []
        self.result = []
    
    def append_node(self, data) :
        n = Node(data)
        if self.head is None : self.head = n
        else :
            t = self.head
            while t.next != None :
                t = t.next
                if t.next == None :
                    n.front = t
            t.next = n

    def print_list(self) :
        p = self.head
        while p != None :
            print(p.data, end=" ")
            p = p.next

    def check_dup(self) :
        curr_node = self.head
        while curr_node != None :
            if curr_node.data not in self.result :
                self.result.append(curr_node.data)
            else :
                self.dup_list.append(curr_node.data)
            curr_node = curr_node.next


data = input("Enter Input : ").split(" ")
data = [int(i) for i in data]

li = List()

for i in data :
    li.append_node(i)

print("Linked list now is ", end="")
li.print_list()
li.check_dup()
print()
print(f"there are {len(li.dup_list)} duplicates that been remove")
print("Remove duplicates Linked list ", end="")
for i in li.result :
    print(i, end=" ")