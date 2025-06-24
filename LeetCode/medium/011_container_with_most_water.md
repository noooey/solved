# 011. Container With Most Water

## Code (Python)
```python3
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        amount = 0
        while left < right:
            width = right - left
            amount = max(amount, width * min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return amount
```

## Complexity
- Time: O(n)

## Notes
- Two-pointer
