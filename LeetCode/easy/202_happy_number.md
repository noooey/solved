# 202. Happy Number

## Code (Python)
```python3
class Solution:
    def isHappy(self, n: int) -> bool:
        dic = {x:x**2 for x in range(10)}
        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            tmp = 0
            for c in str(n):
                tmp += dic[int(c)]
            n = tmp

        return True
```

## Complexity
- Time: O(log n)

## Notes
- HashMap
