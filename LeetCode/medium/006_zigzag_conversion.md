# 006. Zigzag Conversion

## Code (Python)
```python3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows >= n:
            return s
        zigzag = []
        cycle = 2 * numRows - 2

        # first row
        for i in range(0, n, cycle):
            zigzag.append(s[i])

        # middle row
        for j in range(1, numRows - 1):
            left = cycle - 2 * j
            right = 2 * j
            idx = j
            toggle = True
            while idx < n:
                zigzag.append(s[idx])
                idx += left if toggle else right
                toggle = not toggle

        # last row
        for i in range(numRows - 1, n, cycle):
            zigzag.append(s[i])

        return ''.join(zigzag)
```

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
- Simulation

- handle edge case first
- compute cycle
- add characters row by row
