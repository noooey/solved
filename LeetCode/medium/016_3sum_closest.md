# 016. 3Sum Closest

## Code (Python)
```python3
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    return total

                if abs(target - total) < abs(target - closest):
                    closest = total

        return closest
```

## Complexity
- Time: O(n^2)

## Notes
- Two-pointer
