# 058. Length of Last Word

## Code (Python)
```python3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        item_list = s.split(' ')
        for i in range(len(item_list)-1, -1, -1):
            leng = len(item_list[i])
            if leng > 0:
                return leng
        return item_list
```

## Complexity
- Time: O(n)

## Notes
- Indexing
