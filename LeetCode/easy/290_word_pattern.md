# 290. Word Pattern

## Code (Python)
```python3
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic_by_pattern = {}
        dic_by_word = {}
        words = s.split()
        if len(words) != len(pattern):
            return False
        for p, w in zip(pattern, words):
            if p in dic_by_pattern:
                if dic_by_pattern[p] != w:
                    return False
                if dic_by_word[w] != p:
                    return False
            else:
                if w in dic_by_word:
                    return False
                dic_by_pattern[p] = w
                dic_by_word[w] = p
        return True
```

## Complexity
- Time: O(n)

## Notes
- HashMap
