class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = (key, value)

    def get(self, key):
        index = self._hash(key)
        start_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start_index:
                break
        return None


# 테스트
ht = OpenAddressingHashTable()
ht.insert("name", "Kyu")
ht.insert("age", 25)
print(ht.get("name"))  # "Kyu"
print(ht.get("age"))   # 25
