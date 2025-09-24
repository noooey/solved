# 151. Reverse Words in a String

## Code (Python)
```python3
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        return " ".join(reversed(words))
```

## Complexity
- Time: O(n)
- Space: O(n)

## Notes
- String

- remove blank on left and right side
- split the sentence by blank and transform into a list
- iterate from the last word.
