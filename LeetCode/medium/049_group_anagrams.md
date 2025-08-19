# 049. Group Anagrams

## Code (Python)
```python3
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            groups[key].append(word)
        return list(groups.values())

```

## Complexity
- Time: O(n·k log k)

## Notes
- default dict
