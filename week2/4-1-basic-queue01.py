class Queue :
    def __init__(self) :
        self.queue = []
        self.shape = 0

    def enQ(self, i) :
        print(f"Add {i} index is {self.shape}")
        self.shape += 1
        self.queue.append(i)

    def deQ(self) :
        if self.shape == 0 : 
            print(-1)
            return
        self.shape -= 1
        print(f"Pop {self.queue[0]} size in queue is {self.shape}")
        item = self.queue.pop(0)
        return item
    
    def size(self) :
        return self.shape
    
    
data = input("Enter Input : ").split(",")
data = [i.split(" ") for i in data]

q = Queue()

for i in data :
    if i[0] == 'E' :
        q.enQ(i[1])
    elif i[0] == 'D' :
        q.deQ()

if q.shape == 0 : print("Empty")
else : print(f"Number in Queue is :  {q.queue}")
