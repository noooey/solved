T = int(input())
for i in range(T):
    total = 0
    N = int(input())
    for j in range(N):
        A, B, C = map(int, input().split())
        max = A
        if B > A:
            max = B
            if C > max:
                max = C
        elif C > A:
            max = C
        if max > 0:
            total += max
        # A, B, C 주식 중 가장 큰 값이면서 그 값이 양수이면 total에 더함

    print(total)