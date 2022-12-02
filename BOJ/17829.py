N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def pulling(mtx):
    lst3 = []
    for i in range(int(len(mtx)/2)):
        lst2 = []
        for j in range(int(len(mtx)/2)):
            lst = []   # 2*2짜리 행렬의 리스트 생성
            lst.append(mtx[2*i][2*j])
            lst.append(mtx[2*i][2*j+1])
            lst.append(mtx[2*i+1][2*j])
            lst.append(mtx[2*i+1][2*j+1])

            lst.sort()
            lst2.append(lst[2])  # 리스트에서 두 번째로 큰 요소

        lst3.append(lst2)

    if len(lst3) > 1:
        return pulling(lst3)
    else:
        return lst3[0][0]

print(pulling(matrix))