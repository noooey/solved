# 053. Maximum Subarray

## Code (Python)
```python3
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -sys.maxsize
        cur_sum = 0
        best_l, best_r = 0, 0
        l = 0
        for i, x in enumerate(nums):
            if cur_sum + x < x:
                cur_sum = x
                l = i
            else:
                cur_sum += x

            if cur_sum > max_sum:
                max_sum = cur_sum
                best_l, best_r = l, i

        return max_sum
```

## Complexity
- Time: O(n)

## Notes
- Kadane
