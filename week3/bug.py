class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class LinkList:
    def __init__(self, head=None):
        self.head = head
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def removeHead(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def removeTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        
    def insertAfter(self, i, data):
        new_node = Node(data)
        temp = self.head 
        count = 0
        while temp is not None:
            if count == i: 
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            count += 1
            
    def searchIndexByData(self, data):
        temp = self.head
        count = 0
        while temp is not None:
            if temp.data == data:
                return count
            count += 1
            temp = temp.next
        return
    
    def searchDataByIndex(self, i):
        temp = self.head
        count = 0
        while temp is not None:
            if count == i:
                return temp.data
            count += 1
            temp = temp.next
        return None
    
    def sizeOfLinkList(self):
        temp = self.head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
            
    def display(self):
        temp = self.head
        if temp is None:
            return
        while temp is not None:
            if temp.next is None:
                print(temp.data)
            else:
                print(temp.data, end=" -> ")
            temp = temp.next
            
def trainDirection(word):
    word = word.split("/")
    stations = word[0].strip().split(",")
    operations = word[1].strip().split(",")
    
    myLinkList = LinkList()
    for station in stations:
        myLinkList.append(station.strip())
    
    start = operations[0].strip()
    end = operations[1].strip()
    direction = operations[2].strip() if len(operations) > 2 else None
    
    start_index = myLinkList.searchIndexByData(start)
    end_index = myLinkList.searchIndexByData(end)
    size = myLinkList.sizeOfLinkList()
    forward_check_points = list(range(start_index, size)) + list(range(0, start_index))
    backward_check_points = list(range(0, start_index+1))[::-1] + list(range(start_index+1, size))[::-1]

    def get_route_points(check_points, end_index):
        route_points = []
        for i in check_points:
            route_points.append(myLinkList.searchDataByIndex(i))
            if i == end_index:
                break
        return route_points
    
    if direction == "F":
        forward_route = get_route_points(forward_check_points, end_index)
        print(f"Forward Route: {'->'.join(forward_route)},{len(forward_route) - 1}")
    elif direction == "B":
        backward_route = get_route_points(backward_check_points, end_index)
        print(f"Backward Route: {'->'.join(backward_route)},{len(backward_route) - 1}")
    else:
        forward_route = get_route_points(forward_check_points, end_index)
        backward_route = get_route_points(backward_check_points, end_index)
        if len(forward_route) < len(backward_route):
            print(f"Forward Route: {'->'.join(forward_route)},{len(forward_route) - 1}")
        elif len(forward_route) > len(backward_route):
            print(f"Backward Route: {'->'.join(backward_route)},{len(backward_route) - 1}")
        else:
            print(f"Forward Route: {'->'.join(forward_route)},{len(forward_route) - 1}")
            print(f"Backward Route: {'->'.join(backward_route)},{len(backward_route) - 1}")

print("***Railway on route***")
word = input("Input Station name/Source, Destination, Direction(optional): ").strip()
trainDirection(word)