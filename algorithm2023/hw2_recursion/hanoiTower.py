def move():


def hanoiTower(n, k, cnt):

    if k == cnt[0]:
        return source, target

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    cnt = [0]
    print(*hanoiTower(n, k, cnt))
