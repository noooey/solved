def sosu(m):
    for i in range(2, m+1):
        if m % i == 0:
            return i

def solution(n):
    size = n
    size_list = []
    while size > 3:
        size = size // sosu(size)
        size_list.append(size)
    print(size_list)



    answer = []
    return ' '.join(map(str, answer))

t = int(input())
for _ in range(t):
    N = int(input())
    print(solution(N))

'''
1 2 3 4 5 6 7 8
1 3 5 7/2 4 6 8
1 5/3 7/2 6/4 8
'''
