# 026. Remove Duplicates from Sorted Array

## Code (Python)
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx
```

## Complexity
- Time: O(n)

## Notes
- Two pointer
