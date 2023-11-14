def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    split_points = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            memo[i][j] = float('inf')
            for k in range(i, j):
                cost = memo[i][k] + memo[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if cost < memo[i][j]:
                    memo[i][j] = cost
                    split_points[i][j] = k

    return memo[1][n], split_points

def print_matrix_expression(split_points, i, j):
    if i == j:
        return f'M{i}'
    else:
        return f'({print_matrix_expression(split_points, i, split_points[i][j])}' \
               f'{print_matrix_expression(split_points, split_points[i][j] + 1, j)})'

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().split()))
        result, split_points = matrix_chain_multiplication(values)
        expression = print_matrix_expression(split_points, 1, n)
        print(expression)
        print(result)

if __name__ == "__main__":
    main()
