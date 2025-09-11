# 075. Sort Colors

## Code (Python)
```python3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        colors = [0, 0, 0]   # red white blue
        for num in nums:
            if num == 0:
                colors[0] += 1
            elif num == 1:
                colors[1] += 1
            else:
                colors[2] += 1

        c_idx = 0
        for c in range(len(colors) - 1):
            while c_idx < n and nums[c_idx] == c:
                c_idx += 1

            i = n - 1
            while i > c_idx:   # 뒤에서부터 순회
                if nums[i] == c:
                    nums[i], nums[c_idx] = nums[c_idx], nums[i]
                    c_idx += 1
                while c_idx < n and nums[c_idx] == c:
                    c_idx += 1

                if c_idx == sum(colors[:c + 1]):
                    break

                i -= 1
```

## Complexity
- Time: O(n)

## Notes
- Two Pointer
