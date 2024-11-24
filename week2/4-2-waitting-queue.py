data = input("Enter people and time : ").split(" ")
people = [c for c in data[0]]
time = int(data[1])

class Queue :
    def __init__(self, ls=None) :
        if ls == None : self.queue = []
        else : self.queue = ls
        
    def push(self, i) :
        self.queue.append(i)

    def pop(self) :
        if len(self.queue) == 0 : return
        item = self.queue.pop(0)
        return item
    
    def data(self) :
        return self.queue
    
    def isFull(self) :
        return len(self.queue) == 5

q1 = Queue()
q2 = Queue()
q_people = Queue(people)

for i in range(1, time + 1) :
    if (i - 1) % 3 == 0 : q1.pop()

    p = q_people.pop()
    if not q1.isFull() :
        if p != None : q1.push(p)
    else :
        if p != None : q2.push(p)
    print(f"{i} {q_people.data()} {q1.data()} {q2.data()}")
    if i >= 9 and (i - 1) % 2 == 0 : q2.pop()
