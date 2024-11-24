print(" ***** Fun with hashing *****")

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:

    def __init__(self, size, max_collision) :
        self.table = [None for i in range(size)]
        self.size = size
        self.item = 0
        self.max_collision = max_collision 

    def hash_function(self, key) :
        hash_index = 0
        for i in key :
            hash_index += ord(i)
        hash_index %= self.size

        return hash_index

    def add(self, data: Data) :
        colli = 0
        index = self.hash_function(data.key)
        add = False
        while colli < self.max_collision :
            if self.table[(index + colli ** 2) % self.size] == None : 
                self.table[(index + colli ** 2) % self.size] = data
                add = True
                self.item += 1
                break
            colli += 1
            print(f"collision number {colli} at {(index + (colli - 1) ** 2) % self.size}")
        if add : 
            self.printData()
            print("---------------------------")
        else : 
            print("Max of collisionChain")
            self.printData()
            print("---------------------------")
    def isFull(self) :
        return self.item == self.size
    
    def printData(self) :
        for i in range(self.size) :
            print(f"#{i + 1}	{self.table[i]}")
    
inp = input("Enter Input : ").split("/")
init_hash_size, init_hash_max_collision = tuple(map(int, (inp[0].split(" "))))
data = inp[1].split(",")
data_lst = []
for i in data :
    item = i.split(" ")
    data_lst.append(Data(item[0], item[1]))


h1 = hash(init_hash_size, init_hash_max_collision)
for i in data_lst :
    if not h1.isFull() : h1.add(i)
    else : 
        print("This table is full !!!!!!")
        break



