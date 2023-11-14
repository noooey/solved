def matrix_chain_multiplication(dimensions, i, j, memo):
    if i == j:
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    min_operations = float('inf')

    for k in range(i, j):
        operations = matrix_chain_multiplication(dimensions, i, k, memo) + \
                     matrix_chain_multiplication(dimensions, k + 1, j, memo) + \
                     dimensions[i - 1] * dimensions[k] * dimensions[j]

        min_operations = min(min_operations, operations)

    memo[i][j] = min_operations
    return min_operations

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().split()))
        memo = [[-1] * (n+1) for _ in range(n+1)]
        print(matrix_chain_multiplication(values, 1, n, memo))

if __name__ == "__main__":
    main()
