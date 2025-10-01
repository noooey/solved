# 205. Isomorphic Strings

## Code (Python)
```python3
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map = {}
        t_map = {}
        for sc, tc in zip(s, t):
            if sc in s_map:
                if s_map[sc] != tc:
                    return False
            else:
                if tc in t_map:
                    return False
                s_map[sc] = tc
                t_map[tc] = sc
        return True
```

## Complexity
- Time: O(n)

## Notes
- HashMap
