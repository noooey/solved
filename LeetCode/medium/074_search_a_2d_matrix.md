# 074. Search a 2D Matrix

## Code (Python)
```python3
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        cs, ce = 0, n - 1

        if target < matrix[cs][0] or target > matrix[ce][m - 1]:
            return False

        if target >= matrix[n - 1][0]:
            cs = n - 1
        else:
            while cs < ce:
                mid = (cs + ce) // 2
                if target < matrix[mid][0]:
                    ce = mid - 1
                elif target > matrix[mid][m - 1]:
                    cs = mid + 1
                else:
                    cs = mid
                    break
        print(cs, ce)

        if target < matrix[cs][0] or target > matrix[cs][m - 1]:
            return False

        rs, re = 0, m - 1
        while rs <= re:
            mid = (rs + re) // 2
            if target < matrix[cs][mid]:
                re = mid - 1
            elif target > matrix[cs][mid]:
                rs = mid + 1
            else:
                return True
        return False
```

## Complexity
- Time: O(logn+logm)

## Notes
- Binary Search
