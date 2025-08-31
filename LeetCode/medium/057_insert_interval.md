# 057. Insert Interval

## Code (Python)
```python3
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        new_arr = [intervals[0]]
        for a, b in intervals[1:]:
            i, j = new_arr.pop()
            if a in range(i, j + 1):
                if b > j:
                    new_arr.append([i, b])
                else:
                    new_arr.append([i, j])      
            else:
                new_arr.append([i, j])
                new_arr.append([a, b])  
        return new_arr
```

## Complexity
- Time: O(n)

## Notes
- Indexing
