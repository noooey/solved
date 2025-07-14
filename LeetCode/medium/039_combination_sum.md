# 039. Combination Sum

## Code (Python)
```python3
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(start, path, total):
            if total == target:
                results.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return results
```

## Complexity
- Time: 

## Notes
- Back-tracking, Recursion
