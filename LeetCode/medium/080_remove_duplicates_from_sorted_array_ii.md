# 080. Remove Duplicates from Sorted Array II

## Code (Python)
```python3
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n

        k, i = 1, 2
        while i < n:
            if nums[k] == nums[i]:
                if nums[k] != nums[k - 1]:
                    k += 1
                    nums[k] = nums[i]
            else:
                k += 1
                nums[k] = nums[i]
            i += 1
        k += 1
        return k
```

## Complexity
- Time: O(n)

## Notes
- Two-pointer
