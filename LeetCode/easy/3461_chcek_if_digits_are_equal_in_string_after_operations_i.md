# 3461. Check If Digits Are Equal in String After Operations I

## Code (Python)
```python3
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        num = str(s)
        while len(num) > 2:
            tmp = ''
            for i in range(len(num) - 1):
                n = (int(num[i]) + int(num[i+1])) % 10
                tmp += str(n)
            if len(tmp) == 2:
                if tmp[0] == tmp[1]:
                    return True
            num = tmp
        return False
```

## Complexity
- Time: O(n^2)

## Notes
- Array
