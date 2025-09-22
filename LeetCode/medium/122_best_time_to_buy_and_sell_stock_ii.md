# 122. Best Time to Buy and Sell Stock II

## Code (Python)
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        benefit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                benefit += (prices[i] - prices[i - 1])
        return benefit
```

## Complexity
- Time: O(n)

## Notes
- Array
