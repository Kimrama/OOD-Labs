data = input("input : ").split(",")

class Queue :
    def __init__(self) :
        self.queue = []
        self.err_deq = 0
        self.err_input = 0
        self.last = -1
        self.shape = 0

    def enQ(self, data) :
        for i in range(int(data[1::])) :
            self.last += 1
            self.shape += 1
            self.queue.append(f"*{self.last}")
        print(f"Step : {data}")
        print(f"Enqueue : {self.queue}")
        print(f"Error Dequeue : {self.err_deq}")
        print(f"Error input : {self.err_input}")
        print("--------------------")

    def deQ(self, data) :
        for i in range(int(data[1::])) :
            if self.shape == 0 : self.err_deq += 1
            else :
                self.shape -= 1
                self.queue.pop(0)
        print(f"Step : {data}")
        print(f"Dequeue : {self.queue}")
        print(f"Error Dequeue : {self.err_deq}")
        print(f"Error input : {self.err_input}")
        print("--------------------")

    def input_error(self, data) :
        self.err_input += 1
        print(f"Step : {data}")
        print(f"{self.queue}")
        print(f"Error Dequeue : {self.err_deq}")
        print(f"Error input : {self.err_input}")
        print("--------------------")

q = Queue()

for i in data :
    if i[0] == 'E' :
        q.enQ(i)
    elif i[0] == 'D' :
        q.deQ(i)
    else :
        q.input_error(i)