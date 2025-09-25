# 125. Valid Palindrome

## Code (Python)
```python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while 0 <= i < len(s) and 0 <= j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if i == len(s):
            return True
        return False
```

## Complexity
- Time: O(n)

## Notes
- Array

- move forward by matching condition
