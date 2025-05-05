# 013. Roman to Integer

## Code (Python)
```python3
class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        value = 0
        i = 0
        while i < len(s):
            if i < len(s) - 1:
                if symbols[s[i]] < symbols[s[i+1]]:
                    value += symbols[s[i+1]] - symbols[s[i]]
                    i += 2
                    continue
            value += symbols[s[i]]
            i += 1
        return value
```

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
- HashMap + One-pass
