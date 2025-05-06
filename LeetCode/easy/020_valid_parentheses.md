# 020. Valid Parentheses

## Code (Python)
```python3
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = deque([])
        for b in s:
            if b in brackets:
                if not stack or stack.pop() != brackets[b]:
                    return False
            else:
                stack.append(b)
        return not stack
```

## Complexity
- Time: O(n)

## Notes
- Stack
