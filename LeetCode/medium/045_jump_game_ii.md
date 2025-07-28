# 045. Jump Game II

## Code (Python)
```python3
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        cur_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == cur_end:
                cnt += 1
                cur_end = farthest

        return cnt
```

## Complexity
- Time: O(n)

## Notes
- Greedy
- 정확하게 index n-1에 도달할 필요가 없다.
