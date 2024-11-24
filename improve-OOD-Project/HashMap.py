# HashMap.py
class HashTable:
    def __init__(self, size: int = 100):
        self.size = size
        self.table = [None] * self.size

    def hash1(self, key) -> int:
        return key % self.size

    def hash2(self, key) -> int:
        prime = self.size - 1
        return prime - (key % prime)

    def insert(self, key, value):
        index = self.hash1(key)
        step_size = self.hash2(key)
        i = 0

        # Double Hashing to find empty slot
        while self.table[index] is not None and self.table[index][0] != key:
            i += 1
            index = (self.hash1(key) + i * step_size) % self.size
            # ตรวจสอบว่าการ probing ไม่วนกลับมา index เดิม
            if i >= self.size:
                raise Exception("HashTable is full, cannot insert.")

        self.table[index] = (key, value)

    def search(self, key):
        index = self.hash1(key)
        step_size = self.hash2(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            i += 1
            index = (self.hash1(key) + i * step_size) % self.size
            # เพิ่มการตรวจสอบเพื่อป้องกันการวนซ้ำ
            if i >= self.size:
                break
        return None

    def remove(self, key):
        index = self.hash1(key)
        step_size = self.hash2(key)
        i = 0

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            i += 1
            index = (self.hash1(key) + i * step_size) % self.size
            if i >= self.size:
                break
        return False
