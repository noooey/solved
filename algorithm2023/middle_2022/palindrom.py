def palindrom(n, values, i, j):
    print(f'values[{i}]:{values[i]} | values[{j}]:{values[j]}')
    if n == 1:
        return 1
    else:
        odd = n % 2 # 0이면 짝수, 1이면 홀수
        if odd:
            if i + 2 == j:
                return 1 if values[i] == values[j] else 0
        else:
            if i + 1 == j:
                return 1 if values[i] == values[j] else 0
    if values[i] == values[j]:
        return 1 * palindrom(n, values, i+1, j-1)
    else:
        return 0

t = int(input())
for _ in range(t):
    n, *values = map(int, input().split())
    print(palindrom(n, values, 0, n-1))
