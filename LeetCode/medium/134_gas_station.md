# 134. Gas Station

## Code (Python)
```python3
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            if tank < 0:
                start = i + 1
                tank = 0

        return start
```

## Complexity
- Time: O(n)
- Space: O(1)

## Notes
- Greedy

- When the tank becomes negative, the car must stop → find the first index where the running tank never goes negative.
- If the total cost is greater than the total gas, no solution exists.
- Since the whole trip has a non-negative total balance, finishing the right side already proves the left side will also work when wrapping around.


"""
gas = [0]
cost = [0]
left = [0]

gas = [1, 1, 1, 0, 2, 0, 5]
cost =[0, 0, 0, 5, 0, 5, 0]
left =[1, 1, 1, -5, 2, -5, 5]

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
left = [-2, -2, -2, 3, 3]
"""
