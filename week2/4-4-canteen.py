

data = input("Enter Input : ").split("/")
group_data = [i.split(" ") for i in data[0].split(",")]
group_dict = {}

for i in group_data :
    if i[0] not in group_dict.keys() : group_dict.update({i[0]: [i[1]]})
    else : group_dict[i[0]].append(i[1])

input_seq = [i.split(" ") for i in data[1].split(",")]

class Queue :
    def __init__(self) :
        self.queue = []
        self.shape = 0

    def find_index_of_last_in_group(self, id) :
        for index in range(len(self.queue) - 1, 0, -1) :
            for i in group_dict.items() :
                if id in i[1] and self.queue[index - 1] in i[1] : 
                    return index


    def enQ(self, id) :
        if self.shape == 0 : self.queue.append(id)
        else :
            last_index = self.find_index_of_last_in_group(id)
            if last_index == None : last_index = len(self.queue)
            self.queue.insert(last_index, id)
        self.shape += 1

    def deQ(self) :
        self.shape -= 1
        return self.queue.pop(0)
    
    def isEmpty(self) :
        return self.shape == 0

q = Queue()

for i in input_seq :
    if i[0] == 'E' :
        q.enQ(i[1])
    elif i[0] == 'D' :
        if q.isEmpty() : print("Empty")
        else : 
            item = q.deQ()
            print(item)
