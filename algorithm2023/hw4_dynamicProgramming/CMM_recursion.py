def matrix_chain_multiplication(dimensions, i, j):
    if i == j:
        return 0

    min_operations = float('inf')

    for k in range(i, j):
        operations = matrix_chain_multiplication(dimensions, i, k) + \
                     matrix_chain_multiplication(dimensions, k + 1, j) + \
                     dimensions[i - 1] * dimensions[k] * dimensions[j]

        min_operations = min(min_operations, operations)

    return min_operations

def main():
    t = int(input())
    for _ in range(t):
        n, *values = map(int, input().split())
        print(matrix_chain_multiplication(values, 1, n))

if __name__ == "__main__":
    main()
