# 046. Permutations

## Code (Python)
```python3
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        for per in permutations(nums, n):
            result.append(list(per))
        return result
```

## Complexity
- Time: O(n!)

## Notes
- Permutation
