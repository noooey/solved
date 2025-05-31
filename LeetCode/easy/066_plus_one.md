# 066. Plus One

## Code (Python)
```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        increment = int(''.join(map(str, digits))) + 1
        return [int(n) for n in str(increment)]
```

## Complexity
- Time: O(n)

## Notes
- Iterator
