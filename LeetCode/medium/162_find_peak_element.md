# 162. Find Peak Element

## Code (Python)
```python3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == 2:
            return 0 if nums[0] >= nums[1] else 1
        
        i, j = 0, len(nums) - 1
        peak = nums[0]
        while i < j:
            mid = (i + j) // 2
            if nums[mid + 1] >= nums[mid]:
                i = mid + 1
            else:
                j = mid
        return i
```

## Complexity
- Time: O(n)

## Notes
- Binary Search
