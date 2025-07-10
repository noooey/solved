# 036. Valid Sudoku

## Code (Python)
```python3
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        subs = [[set() for _ in range (n // 3)] for _ in range (n // 3)]
        for i in range(n):
            for j in range(n):
                if board[i][j] in cols[i]:
                    # print(f'1 board[{i}][{j}]: {board[i][j]}')
                    return False
                if board[i][j] in rows[j]:
                    # print(f'2 board[{i}][{j}]: {board[i][j]}')
                    return False
                if board[i][j] in subs[i//3][j//3]:
                    # print(f'3 board[{i}][{j}]: {board[i][j]}')
                    return False
                if board[i][j] != '.':
                    cols[i].add(board[i][j])
                    rows[j].add(board[i][j])
                    subs[i//3][j//3].add(board[i][j])
        return True
```

## Complexity
- Time: O(n**2)

## Notes
- Array
