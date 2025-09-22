# 380. Insert Delete GetRandom O(1)

## Code (Python)
```python3
class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.pos = {}


    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.arr.append(val)
            self.pos[val] = len(self.arr) - 1
            return True
        return False


    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx = self.pos[val]
        last = self.arr[-1]
        self.arr[idx] = last
        self.pos[last] = idx
        self.arr.pop()
        del self.pos[val]
        return True


    def getRandom(self) -> int:
        return self.arr[random.randrange(len(self.arr))]
```

## Complexity
- Time: O(1)

## Notes
- HashMap
