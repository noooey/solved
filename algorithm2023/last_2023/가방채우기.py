t = int(input())
for _ in range(t):
    n, W = map(int, input().split())
    string = list(map(int, input().split()))
    cheeses = []
    for i in range(0, len(string)-1, 2):
        cheeses.append((string[i], string[i+1]))

    # 단위부피 가격 싼 기준 정렬
    cheeses = sorted(cheeses, key=lambda x: x[1]//x[0], reverse=True)

    dp = [[0]*(W+1) for _ in range(n)]

    # init
    for i in range(n):
        s, v = cheeses[i]
        for j in range(s, W+1):
            dp[i][j] = v

    for i in range(1, n):
        for j in range(1, W+1):
            cur_s = cheeses[i][0]
            cur_v = cheeses[i][1]

            if j >= cur_s:
                dp[i][j] = max(dp[i-1][j-cur_s] + cur_v, dp[i-1][j])

    best = 0
    for i in range(n):
        for j in range(1, W+1):
            best = max(dp[i][j], best)
    print(best)
