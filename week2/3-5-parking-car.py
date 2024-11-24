class Stack :
    def __init__(self) :
        self.cars = []
        self.i = 0

    def push(self, i) :
        self.cars.append(i)
        self.i += 1

    def pop(self, position) :
        car = self.pop(position)
        self.i -= 1
        return car
    
    def size(self) :
        return self.i

print("******** Parking Lot ********")
data = input("Enter max of car,car in soi,operation : ").split(" ")
max_size = int(data.pop(0))
cars = [int(i) for i in data.pop(0).split(",")]
op = data.pop(0)
op_car = int(data.pop(0))

if cars[0] == 0 : cars = []

s = Stack()

if op == 'arrive' :
    if len(cars) + 1 > max_size : print(f"car {op_car} cannot arrive : Soi Full\n{cars}")
    elif op_car in cars : print(f"car {op_car} already in soi\n{cars}")
    else : 
        cars.append(op_car)
        print(f"car {op_car} arrive! : Add Car {op_car}\n{cars}")

elif op == 'depart' :
    if len(cars) == 0 : print(f"car {op_car} cannot depart : Soi Empty\n{cars}")
    elif op_car not in cars : print(f"car {op_car} cannot depart : Dont Have Car {op_car}\n{cars}")
    elif op_car in cars :
        cars.remove(op_car)
        print(f"car {op_car} depart ! : Car {op_car} was remove\n{cars}")
