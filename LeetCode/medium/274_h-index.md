# 274. H-Index


## Code (Python)
```python3
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        lo, hi = 0, n    
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:
                hi = mid
            else:
                lo = mid + 1
        return n - lo
```

## Complexity
- Time: O(n)

## Notes
- Binary Search
