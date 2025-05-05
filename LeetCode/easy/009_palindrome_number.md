# 009. Palindrome Number

## Code (Python)
```python3
from collections import deque

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = str(x)
        queue = deque(nums)
        while len(queue) > 1:
            if queue.popleft() != queue.pop():
                return False
        return True
```
- deque

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        nums = str(x)
        l, r = 0, len(nums) - 1
        while r > l:
            if nums[l] != nums[r]:
                return False
            r -= 1
            l += 1
        return True
```
- index

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
- Use two-pointer approach for O(n) time
- **Optimization**: Use interger operations directly instead of string conversion (avoid `str(x)`)
