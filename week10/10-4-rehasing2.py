class Hash :
    def __init__(self, size, maxColli, trsh) :
        self.size = size
        self.maxColli = maxColli
        self.trsh = trsh
        self.used = 0
        self.table = [None for i in range(size)]

        print("Initial Table :")
        for i in range(self.size) :
            print(f"#{i + 1}	{self.table[i]}")
        print("----------------------------------------")

    def print_hash(self) :
        for i in range(self.size) :
            print(f"#{i + 1}	{self.table[i]}")
        print("----------------------------------------")

    def add(self, data) :
        colli_tm = 0
        index = self.hash_function(data)
        while True :
            if self.table[(index + colli_tm ** 2) % self.size] is None :
                if self.hit_treshole() :
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehasing()
                    index = self.hash_function(data)
                    continue
                else : 
                    self.table[(index + colli_tm ** 2) % self.size] = data
                    self.used += 1
                    break
            else :
                print(f"collision number {colli_tm + 1} at {(index + colli_tm ** 2) % self.size}")
                colli_tm += 1

                if colli_tm == self.maxColli :
                    print("****** Max collision - Rehash !!! ******")
                    self.rehasing()
                    index = self.hash_function(data)
                    colli_tm = 0
                    continue
        self.print_hash()

    def add_rehash(self, data) :
        colli_tm = 0
        index = self.hash_function(data)
        while True :
            if self.table[(index + colli_tm ** 2) % self.size] is None :
                if self.hit_treshole() :
                    print("****** Data over threshold - Rehash !!! ******")
                    self.rehasing()
                    index = self.hash_function(data)
                    continue
                else : 
                    self.table[(index + colli_tm ** 2) % self.size] = data
                    self.used += 1
                    break
            else :
                print(f"collision number {colli_tm + 1} at {(index + colli_tm ** 2) % self.size}")
                colli_tm += 1

                if colli_tm == self.maxColli :
                    print("****** Max collision - Rehash !!! ******")
                    self.rehasing()
                    index = self.hash_function(data)
                    colli_tm = 0
                    continue

    def hit_treshole(self) :
        return (self.used + 1) / self.size * 100 >= self.trsh

    def rehasing(self) :
        # print(self.table[::-1])
        temp = [i for i in self.table[::-1] if i is not None]
        self.used = 0
        self.set_next_size()
        self.table = [None for i in range(self.size)]
        for i in temp :
            self.add_rehash(i)
            

    @staticmethod
    def is_prime(data) :
        for i in range(2, data // 2) :
            if data % i == 0 : return False
        return True
    
    def set_next_size(self) :
        self.size = self.size * 2
        while True :
            if self.is_prime(self.size) : break
            else : self.size += 1
                
    def hash_function(self, data) :
        return data % self.size
    

print(" ***** Rehashing *****")
inp = input("Enter Input : ")
init_hash_data = list(map(int, inp.split("/")[0].split(" ")))
add_data = list(map(int, inp.split("/")[1].split(" ")))

h = Hash(init_hash_data[0], init_hash_data[1], init_hash_data[2])
for i in add_data :
    print(f"Add : {i}")
    h.add(i)