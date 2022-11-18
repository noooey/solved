import sys
input = sys.stdin.readline

cnt_0 = [1, 0, 1]
cnt_1 = [0, 1, 1]

def fibo(n):
    if n == 0:
        print(f'{cnt_0[0]} {cnt_1[0]}')
        return
    elif n == 1:
        print(f'{cnt_0[1]} {cnt_1[1]}')
        return
    elif n == 2:
        print(f'{cnt_0[2]} {cnt_1[2]}')
        return
    else:
        cnt_0.append(cnt_0[n-1] + cnt_0[n-2])
        cnt_1.append(cnt_1[n-1] + cnt_1[n-2])

    print(f'{cnt_0[n-1]} {cnt_1[n-1]}')

t = int(input())
for _ in range(t):
    fibo(int(input()))
