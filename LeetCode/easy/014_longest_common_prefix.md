# 014. Longest Common Prefix

## Code (Python)
```python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            tmp = ""
            for p, w in zip(prefix, word):
                if p == w:
                    tmp += p
                else:
                    break
            prefix = tmp
            if len(prefix) < 1:
                prefix = ""
                break
        return prefix
```

## Complexity
- Time: O(n)

## Notes
- Zip, Trim Prefix
