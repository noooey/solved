# 040. Combination Sum II

## Code (Python)
```python3
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def recursive(start, path, total):
            if total == target:
                results.append(path[:])
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                recursive(i + 1, path + [candidates[i]], total + candidates[i])

        recursive(0, [], 0)
        return results
```

## Complexity
- Time:

## Notes
- Back-tracking, Recursion
