# 034. Find First and Last Position of Element in Sorted Array

## Code (Python)
```python3
import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1

        if left <= right and right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]
```

## Complexity
- Time: O(log n)

## Notes
- Bisect
