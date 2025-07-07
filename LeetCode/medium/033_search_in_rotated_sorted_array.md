# 033. Search in Rotated Sorted Array

## Code (Python)
```python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        cnt = 0
        while cnt < n:
            if nums[i] == target:
                return i if i >= 0 else n + i
            elif nums[i] < target:
                i += 1
            else:
                i -= 1
            cnt += 1
        return -1
```

## Complexity
- Time: O(n)

## Notes
- Array
