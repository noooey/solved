# 055. Jump Game

## Code (Python)
```python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i, step in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + step)
        return True
```

## Complexity
- Time: O(n)

## Notes
- Greedy
