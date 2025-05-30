# 035. Search Insert Position

## Code (Python)
```python3
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1

        return start
```

## Complexity
- Time: O(log n)

## Notes
- Binary Search
