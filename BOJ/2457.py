import sys
input = sys.stdin.readline

MONTH = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
START = 60
END = 334

N = int(input())
flowers = []
for _ in range(N):
    open_month, open_day, close_month, close_day = map(int, input().split())

    open, close = 0, 0
    if open_month > 1:
        for i in range(1, open_month):
            open += MONTH[i]
    open += open_day

    if close_month > 1:
        for i in range(1, close_month):
            close += MONTH[i]
    close += close_day

    if open <= END and close > START:
        flowers.append((open, close))

# open이 빠르고 close가 느린 순서로 정렬
flowers = sorted(flowers, key=lambda x:x[1], reverse=True)
flowers = sorted(flowers, key=lambda x:x[0])
# print(flowers)

cnt = 0
cur_start = START
cur_end = START
for flower in flowers:
    # print(flower)
    if flower[0] <= cur_start:
        cur_end = max(cur_end, flower[1])
        # print(f'end changed: {cur_end}')
    else:
        cur_start = cur_end
        # print(f'start changed: {cur_start}')
        if flower[0] <= cur_start:
            cnt += 1
            cur_end = max(cur_end, flower[1])
            # print(f'end changed: {cur_end}')
    if cur_end > END:
        cnt += 1
        break

if flowers[0][0] > START:
    print(0)
else:
    if cur_end > END:
        print(cnt)
    else:
        print(0)


"""
cur_start ----------- cur_end
cur_start ---------------------- cur_end
cur_start ------------------------------------ cur_end
             cur_start --------------------------------------- cur_end
                            cur_start ------------------------------------ cur_end
                                              cur_start ----------------------------------- cur_end
                                                             cur_start ------- cur_end
"""
