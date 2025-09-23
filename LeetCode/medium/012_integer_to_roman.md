# 012. Integer to Roman

## Code (Python)
```python3
class Solution:
    def intToRoman(self, num: int) -> str:
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        output = ''
        i = 0
        while num > 0 and 0 <= i < len(symbol):
            if num >= value[i]:
                num -= value[i]
                output += symbol[i]
            else:
                i += 1
        return output
```

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
- Greedy

- There are only a few Roman symbols, so I can write them all in a list with their values.
- I start from the biggest value and keep subtracting it from the number, adding its symbol to the answer, until the number becomes 0.
