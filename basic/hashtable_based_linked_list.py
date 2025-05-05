class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size   # Hash function

    def insert(self, key, value):
        index = self._hash(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

ht = HashTable()
ht.insert("name", "Kyu")
ht.insert("age", 25)
print(ht.get("name"))
print(ht.get("age"))
