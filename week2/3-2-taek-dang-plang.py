class Stack :
    def __init__(self) :
        self.data = []
        self.s = 0

    def push(self, i) :
        self.s += 1
        self.data.append(i)

    def pop(self) :
        self.s -= 1
        return self.data.pop()
    
    def top(self) :
        return self.data[self.s - 1]
    
    def size(self) :
        return self.s
    
    def isEmpty(self) :
        return (self.data) == 0


data = input("Enter Input : ")
data = data.split(",")
useable_data = [l.split(" ") for l in data]

stack = Stack()
for i in useable_data :
    if stack.size() == 0 : stack.push(i)
    else :
        if int(i[0]) > int(stack.top()[0]) :
            for j in range(len(stack.data)) :
                if  int(i[0]) > int(stack.top()[0]) :
                    pop = stack.pop()
                    print(pop[1])
            stack.push(i)
        else : stack.push(i)


# 10 5
# 5 5
# 1 2
# 5 5
# 4 4
# 4 4
# 1 2


    