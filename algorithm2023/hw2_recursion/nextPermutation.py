def nextPermutation(n, values):
    c = values
    i = n-2
    while(i >= 0 and c[i] >= c[i+1]):
        i -= 1
    if i == -1:
        return list(reversed(c))
    j = n-1
    while(c[i] > c[j]):
        j -= 1
    c[i], c[j] = c[j], c[i]

    return c[:i+1] + list(reversed(c[i+1:]))

t = int(input())
for _ in range(t):
    n, values = input().split()
    n = int(n)
    print(''.join(nextPermutation(n, list(values))))
