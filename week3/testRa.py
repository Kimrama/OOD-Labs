class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class QueueList:
    def __init__(self):
        self.head = None

    def append(self, data, at_end=True):
        if self.head is None:
            self.head = Node(data)
        else:
            if at_end:
                n = self.head
                while n.next:
                    n = n.next
                n.next = Node(data)
            else:
                n = Node(data)
                n.next = self.head
                self.head = n

    def pop_head(self):
        if self.head:
            head = self.head
            self.head = self.head.next
            return head.data
        return None

    def pop_last(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            head = self.head
            self.head = None
            return head.data
        else:
            n = self.head
            while n.next.next:
                n = n.next
            p = n.next
            n.next = None
            return p.data

    def get_all_items(self):
        res = []
        n = self.head
        while n:
            res.append(n.data)
            n = n.next
        return res

    def is_empty(self):
        return self.head is None
    
    # def insert_head(self, data) :
    #     if self.head == None : self.head = Node(data)
    #     else :
    #         n = Node(data)
    #         n.next = self.head
    #         self.head = n



data = [int(num) for num in input("Enter Input : ").split()]
print("------------------------------------------------------------")
origin = [str(i) for i in data]
queues = [QueueList() for _ in range(20)]

max_num = max(abs(num) for num in data)
max_digits = len(str(max_num))

def position_value(num, position):
    value = abs(num)
    for i in range(position):
        value //= 10
    return value % 10

if len(set(data)) == 1:
    print(f"0 Time(s)")
    print(f"Before Radix Sort : {' -> '.join(origin)}")
    print(f"After  Radix Sort : {' -> '.join(origin)}")
else:
    for digit_place in range(max_digits):
        for num in data:
            digit = position_value(num, digit_place)
            if num >= 0:
                queues[(digit * 2) + 1].append(num)
            else:
                queues[digit * 2].append(num, at_end=False)

        print(f"Round : {digit_place + 1}")
        for i in range(0, 20, 2):
            neg_lis = queues[i].get_all_items()
            pos_lis = queues[i + 1].get_all_items()
            print(f"{int(i / 2)} : {' '.join(map(str, neg_lis + pos_lis))}")
        print("------------------------------------------------------------")
        
        data = []
        for i in range(0, 20, 2):
            while not queues[i].is_empty():
                data.append(queues[i].pop_last())
            while not queues[i + 1].is_empty():
                data.append(queues[i + 1].pop_head())
    
    for num in data:
        digit = position_value(num, max_digits + 1)
        if num >= 0:
            queues[(digit * 2) + 1].append(num)
        else:
            queues[digit * 2].append(num, at_end=False)

    neg_lis = queues[0].get_all_items()
    pos_lis = queues[1].get_all_items()
    data = neg_lis + pos_lis
        

    result = [str(i) for i in data]

    print(f"{max_digits} Time(s)")
    print(f"Before Radix Sort : {' -> '.join(origin)}")
    print(f"After  Radix Sort : {' -> '.join(result)}")