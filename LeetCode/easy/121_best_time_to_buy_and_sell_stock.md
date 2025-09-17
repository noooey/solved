# 121. Best Time to Buy and Sell Stock

## Code (Python)
```python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit
```

## Complexity
- Time: O(n)

## Notes
- Array
