import sys
input = sys.stdin.readline
import heapq

n = int(input())

times = []
for _ in range(n):
    s, t = map(int, input().split())
    heapq.heappush(times, (s, [s, t])) # 수업 시작 빠른 순으로 정렬

rooms = []
while times:
    time = heapq.heappop(times)[1]
    if not rooms:
        heapq.heappush(rooms, time[1])
    else:
        tmp = heapq.heappop(rooms) # 젤 빨리 수업 끝나는 강의실
        if tmp > time[0]: # 강의실 수업 끝나는 시간보다 강의 시작 시간이 먼저라면
            heapq.heappush(rooms, tmp) # pop한거 다시 push
            heapq.heappush(rooms, time[1]) # 새로 강의실 추가
        else:
            heapq.heappush(rooms, time[1]) # 강의실 수업 끝나는 시간 갱신

print(len(rooms))
