# print("***Railway on route***")
# print("Input Station name/Source, Destination, Direction(optional): ", end="")
data = input().split("/")
station_data = data[0].split(",")
process = data[1].split(",")
start = process[0]
stop = process[1]
if len(process) == 3 :
    step = process[2]
else : step = 0

class Node :
    def __init__(self, data, front=None, next=None) :
        if front == None :
            self.front = None
        else : self.front = front

        if next == None :
            self.next = None
        else : self.next = next

        self.data = data

    def __str__(self) : return(f"{self.data}")

class List :
    def __init__(self) :
        self.head = None
        self.trail = None
    
    def append_node(self, data) :
        if self.head == None : self.head = Node(data)
        else :
            t = self.head
            n = Node(data)
            while t.next != None :
                t = t.next
            t.next = n
            n.front = t
            self.trail = n


    def print_list(self) :
        n = self.head
        while n != None :
            print(n)
            n = n.next
    def reach_to_node(self, value) :
        t = self.head
        while t != None :
            if t.data == value : break
            t = t.next
        return t    
    
    def search_by_backward(self, src, des) :
        t = self.reach_to_node(src)
        path_list = []
        while t.front != None :
            path_list.append(t.data)
            if (t.data == des) : return path_list
            t = t.front
        path_list.append(t.data)
        if (t.data == des) : 
            return path_list
        t = self.trail
        while t.front != None :
            path_list.append(t.data)
            if (t.data == des) : return path_list
            t = t.front
        return path_list
    
    def search_by_forward(self, src, des) :
        t = self.reach_to_node(src)
        path_list = []
        while t.next != None :
            path_list.append(t.data)
            if (t.data == des) : return path_list
            t = t.next
        path_list.append(t.data)
        if (t.data == des) : 
            return path_list
        t = self.head
        while t.next != None :
            path_list.append(t.data)
            if (t.data == des) : return path_list
            t = t.next
        return path_list


li = List()

for i in station_data :
    li.append_node(i)

if step == "F" :
    result = li.search_by_forward(start, stop)
    print(f"Forward Route: {"->".join(result)},{len(result) - 1}")
elif step == "B" :
    result = li.search_by_backward(start, stop)
    print(f"Backward Route: {"->".join(result)},{len(result) - 1}")
elif step == 0 :
    result_f = li.search_by_forward(start, stop)
    result_b = li.search_by_backward(start, stop)
    if len(result_f) == len(result_b) :
        print(f"Forward Route: {"->".join(result_f)},{len(result_f) - 1}")
        print(f"Backward Route: {"->".join(result_b)},{len(result_b) - 1}")
    elif len(result_f) > len(result_b) :
        print(f"Backward Route: {"->".join(result_b)},{len(result_b) - 1}")
    else : print(f"Forward Route: {"->".join(result_f)},{len(result_f) - 1}")
