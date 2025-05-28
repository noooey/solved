# 028. Find the Index of the First Occurrence in a String

## Code (Python)
```python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                j = 0
                occur = True
                while j < len(needle):
                    if haystack[i+j] != needle[j]:
                        occur = False
                        break
                    j += 1
                if occur:
                    return i
        return -1
```

## Complexity
- Time: O(n*m)

## Notes
- Brute-force
