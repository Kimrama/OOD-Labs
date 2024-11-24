# main.py
import pandas as pd
import sys
import time
from AVLTree import AVLTree
from HashMap import HashTable

def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"{func.__name__} takes {stop - start:.4f} seconds")
        return result
    return wrapper

class Hotel:
    def __init__(self, size: int = 1000):
        self.avl_tree = AVLTree()
        self.hash_table = HashTable(size)
        self.root = None
        self.max_room_number = 0

    def calculate_room_number(self, fleet: int, ship: int, bus: int, guest: int) -> int:
        return ((fleet+1) ** 7) * ((ship+1) ** 5) * ((bus+1) ** 3) * ((guest+1) ** 2)

    @exec_time
    def add_room(self, fleet: int, ship: int, bus: int, guest: int) -> int:
        room_number = self.calculate_room_number(fleet, ship, bus, guest)
        if self.hash_table.search(room_number) is None:
            self.hash_table.insert(room_number, (fleet, ship, bus, guest))
            self.root = self.avl_tree.insert(self.root, room_number)
            self.max_room_number = max(self.max_room_number, room_number)
        else:
            i = 1
            while self.hash_table.search(room_number) is not None:
                room_number += i ** 2
                i += 1
            self.hash_table.insert(room_number, (fleet, ship, bus, guest))
            self.root = self.avl_tree.insert(self.root, room_number)
            self.max_room_number = max(self.max_room_number, room_number)
        return room_number

    @exec_time
    def remove_room(self, room_number: int):
        if self.hash_table.search(room_number):
            self.hash_table.remove(room_number)
            self.root = self.avl_tree.remove(self.root, room_number)

    @exec_time
    def sort_rooms(self):
        result = []
        self.avl_tree.inorder_traversal(self.root, result)
        return result

    @exec_time
    def find_room(self, room_number: int):
        return self.hash_table.search(room_number)

    @exec_time
    def empty_rooms(self) -> int:
        total_rooms = self.max_room_number
        room_count = sum(1 for item in self.hash_table.table if item is not None)
        return total_rooms - room_count

    @exec_time
    def save_to_file(self, file_name: str):
        data = [(key, value) for key, value in self.hash_table.table if value is not None]
        df = pd.DataFrame(data, columns=["Room Number", "Details"])
        df.to_csv(file_name, index=False)

    def memory_usage(self):
        return sys.getsizeof(self.hash_table) + sys.getsizeof(self.root)

if __name__ == "__main__":
    hotel = Hotel(size=100)

    initial_guest = int(input("Initail Guest: "))
    for i in range(initial_guest):
        hotel.add_room(0, 0, 0, i)

    print(hotel.hash_table)
    while True:
        print("===================================")
        print("MENU: ")
        print("1. add guest")
        print("2. print sort room")
        print("3. print empty room")
        print("4. search room")
        print("5. remove room")
        print("6. save to file")
        print("x. exit..")
        opt = input("select: ")
        if opt == '1':
            n = int(input("Number of guests: "))
            for a in range(n):
                hotel.add_room(0, 0, 0, a)
        elif opt == '2':
            print("Sorted Rooms:", hotel.sort_rooms())
        elif opt == '3':
            print("Empty Rooms:", hotel.empty_rooms())
        elif opt == '4':
            room_number = int(input("Room number: "))
            print(f"Find room {room_number}:", hotel.find_room(room_number))
        elif opt == '5':
            room_number = int(input("Room number: "))
            hotel.remove_room(room_number)
        elif opt == '6':
            hotel.save_to_file("./hotel_rooms.csv")
        elif opt == 'x':
            break
        else:
            print("Invalid selection!")
