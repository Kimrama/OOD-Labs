class Node :
    def __init__(self,data, next=None, front=None):
        self.data = data
        if next == None :
            self.next = None
        else : self.next = next
        if front == None :
            self.front = None
        else : self.front = front

    def __str__(self) :
        return f"{self.data}"


class List :
    def __init__(self, head=None, last=None) :
        if head == None :
            self.head = None
        else : self.head = head
        if last == None :
            self.last = None
        else : self.last = last

    def append_node(self, data) :
        if self.head == None : self.head = Node(data)
        else :
            t = self.head
            while t.next != None :
                t = t.next
            new = Node(data)
            new.front = t
            t.next = new

    def print_list_forward(self) :
        t = self.head
        while t != None :
            print(t.data, end=" ")
            t = t.next

    def print_list_reward(self) :
        t = self.head
        while t.next != None :
            t = t.next
        while t != None :
            print(t.data, end=" ")
            t = t.front


print("Enter Input (L1,L2) : ", end="")
data_input = input().split()
data1 = data_input[0].split("->")
data2 = data_input[1].split("->")

L1 = List()
L2 = List()


for i in data1 :
    L1.append_node(i)

for i in data2 :
    L2.append_node(i)

print(f"L1    : ", end="")
L1.print_list_forward()
print()
print(f"L2    : ", end="")
L2.print_list_forward()
print()
print("Merge : ", end="")
L1.print_list_forward()
L2.print_list_reward()

