# 056. Merge Intervals

## Code (Python)
```python3
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        non_overlapping = []
        for i in range(n):
            if non_overlapping:
                if non_overlapping[-1][1] >= intervals[i][0]:
                    non_overlapping[-1][1] = max(non_overlapping[-1][1], intervals[i][1])
                    continue
            non_overlapping.append(intervals[i])
        return non_overlapping
```

## Complexity
- Time: O(n)

## Notes
- Indexing
