data = input("Enter Input : ").split(",")
data = [i.split(" ") for i in data]
class Stack:

    def __init__(self) :
        self.li = []
        self.i = 0
    def push(self, i) :
        self.li.append(i)
        self.i += 1
    def pop(self) :
        self.i -= 1
        item = self.li.pop()
        return item
    
    def size(self) :
        return self.i
    
    def top(self) :
        return self.li[self.i - 1]

S = Stack()

for i in data :
    if i[0] == 'A' and S.size() == 0 : 
        S.push(i[1])
        continue
    if i[0] == 'A' :
        for j in range(S.size()) :
            if int(S.top()) <= int(i[1]) :
                S.pop()
        S.push(i[1])
    elif i[0] == 'B' :
        print(S.size())




