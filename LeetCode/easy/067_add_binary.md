# 067. Add Binary

## Code (Python)
```python3
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
```

## Complexity
- Time: O(n)

## Notes
- Binary
