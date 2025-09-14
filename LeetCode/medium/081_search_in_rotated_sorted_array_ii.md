# 081. Search in Rotated Sorted Array II

## Code (Python)
```python3
from collections import deque

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        pivot = 0
        for p in range(1, n):
            if nums[p] < nums[p - 1]:
                pivot = p

        queue = deque(nums)
        queue.rotate(-pivot)

        i, j = 0, n - 1
        while i < j:
            mid = (i + j) // 2
            if queue[mid] < target:
                i = mid + 1
            elif queue[mid] > target:
                j = mid - 1
            else:
                return True
        if i == j and queue[i] == target:
            return True
        return False
```

## Complexity
- Time: O(n)

## Notes
- Binary Search
