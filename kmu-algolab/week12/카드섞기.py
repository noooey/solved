import sys
input = sys.stdin.readline


N = 262144
sorted_prime = []
eratos = [1] * (N + 1)
for i in range(2, int((N + 1) ** 0.5) + 1):
    if eratos[i] == 1:
        sorted_prime.append(i)
        temp = i
        while temp < N + 1:
            eratos[temp] = 0
            temp += i


prime = set(sorted_prime)


t = int(input())
for tt in range(t):
    n = int(input())
    factorization = []
    i = 0
    while n not in prime:
        if n % sorted_prime[i] == 0:
            factorization.append(sorted_prime[i])
            n //= sorted_prime[i]
        else:
            i += 1
            if i >= len(sorted_prime):
                break
    factorization.append(n)
    answer = []
    d = 1
    for i in range(len(factorization) - 1):
        d *= factorization[i]
    temp = 1
    for i in range(factorization[-1]):
        answer.append(temp)
        temp += d
    for order in range(len(factorization) - 1):
        d //= factorization[-(2 + order)]
        next = []
        for nn in range(factorization[-(2 + order)] - 1):
            for i in answer:
                next.append(i + d * (nn + 1))
        answer += next
    print(" ".join(map(str, answer)))
