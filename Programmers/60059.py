def turn(m): # 시계방향 90도 회전
    N = len(m)
    new_m = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(N):
            new_m[b][N-1-a] = m[a][b]
    return new_m


def solution(key, lock):
    # lock padding len(key)된 새로운 lock맵 정의, lock hom 개수 저장
    lock_map = [[0]*(len(key)*2+len(lock)) for _ in range(len(key)*2+len(lock))]

    hom = 0
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 1:
                lock_map[i+len(key)][j+len(key)] = 1 # 돌기 표시
            else:
                hom += 1


    # lock 고정, key맵을 이동 및 회전하며 체크
    for _ in range(4): # 360 돌리면서 체크
        # sliding window
        for h in range(len(lock_map)-len(key)+1): # 아래로 순회하면서 체크
            for w in range(len(lock_map)-len(key)+1): # 오른쪽으로 순회하면서 체크
                # key맵 사이즈 window 째로 체크
                cnt = 0
                matched = True
                for oh in range(len(key)):
                    for ow in range(len(key)):
                        if len(key) <= w+ow < len(lock) + len(key) and len(key) <= h+oh < len(lock) + len(key):
                            if lock_map[h+oh][w+ow] + key[oh][ow] != 1:
                                matched = False
                                break
                            elif lock_map[h+oh][w+ow] == 0:
                                cnt += 1
                    if not matched:
                        break
                if matched and hom == cnt:
                    return True
        key = turn(key)

    return False
