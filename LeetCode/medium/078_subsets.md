# 078. Subsets

## Code (Python)
```python3
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        for i in range(n + 1):
            for comb in combinations(nums, i):
                answer.append(comb)
        return answer
```

## Complexity
- Time: O(n 2**n)

## Notes
- Combination
