import heapq

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    orders = [0 for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        orders[Y] = orders[X] + 1
    W = int(input())

    # solutions
    print(orders)

    # 순서배열
    heap = []
    for i in range(1, K+1):
        heapq.heappush(heap, (orders[i], D[i]))

    print(heap)

    # 최소합 구하기
    total = 0 # 현재 값
    cur = 0 # 현재 순서
    while heap:
        tmp = []
        # 현재 순서, value pop
        c, v = heapq.heappop(heap)
        if c == cur:




    # total = 0
    # curr = 0
    # i = 1
    # # 리스트 끝까지 iter 돌면서
    # while i < K+1:
    #     print(f'i: {i} | curr: {curr} | total: {total}')
    #     tmp = []
    #     # 현재 순서 값이랑 현재 iter 값이랑 같다면
    #     if orders[i] == curr:
    #         tmp.append(D[orders[i]])
    #         i += 1
    #     # 같지 않다면 다음 순서로~
    #     else:
    #         print(tmp)
    #         total += min(tmp)
    #         curr += 1
