# 238. Product of Array Except Self

## Code (Python)
```python3
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # zero exist
        zeros = 0
        zero_idx = 0
        # zero non-exist
        all_prod = 1
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
                zero_idx = i
            else:
                all_prod *= num
            if zeros > 1:
                break

        if zeros > 1:
            return [0 for _ in range(n)]

        answer = []
        if zeros == 1:
            for i, num in enumerate(nums):
                if i == zero_idx:
                    answer.append(all_prod)
                else:
                    answer.append(0)
        else:
            for num in nums:
                answer.append(all_prod // num)
        return answer
```

## Complexity
- Time: O(n)

## Notes
- Indexing
