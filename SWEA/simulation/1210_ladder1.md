# 1210. [S/W 문제해결 기본] 2일차 - Ladder1

## Code (Python)
```python3
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, T + 1):
    test_case = int(input())
    n = 100
    axs = [1, -1, 0]
    ays = [0, 0, -1]
    result = 0
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    y = n - 1
    x = grid[n - 1].index(2)
    while y > 0:
        if x - 1 >= 0 and grid[y][x-1] == 1:
            while x - 1 >= 0 and grid[y][x-1] == 1:
                grid[y][x] = 0
                x -= 1
        elif x + 1 < n and grid[y][x+1] == 1:
            while x + 1 < n and grid[y][x+1] == 1:
                grid[y][x] = 0
                x += 1
        else:
            y -= 1

    print(f"#{test_case} {x}")
```

## Complexity
- Time: O(n)

## Notes
- Simulation
