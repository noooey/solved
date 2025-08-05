# 047. Permutations II

## Code (Python)
```python3
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))
```

## Complexity
- Time: O(n!)

## Notes
- Permutation
