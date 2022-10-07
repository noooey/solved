import sys
input = sys.stdin.readline

p = list(input().rstrip()) # 문자열 리스트 변환 시 생기는 오른쪽 개행문자 제거
p_set = set(p) # 리스트 -> 집합: 문자 종류 파악
p_dic = {} # 집합 -> dictionary: 각 문자(key)의 등장 횟수(value)
for c in p_set:
    p_dic[c] = p.count(c)

front = [] # 문자열을 반으로 나눴을 때, 앞부분 -> 추후 좌우반전시켜서 붙이면 팰린드롬
center = [] # 문자열의 가운데 글자
for item in p_dic.items(): # item: (문자, 등장횟수)
    if item[1] % 2 != 0: # 등장횟수가 홀수라면
        ###팰린드롬이 불가능한 문자열 필터링###
        if len(center) != 0: # 그런 문자가 이미 존재한다면 -> 팰린드롬 불가능
            print('I\'m Sorry Hansoo') # 쏘리 한수 출력하고
            exit(0) # 강제종료
        ################################
        center.append(item[0]) # 문자열의 가운데 글자로 지정
        front.append(item[0]*((item[1]-1)//2)) # 가운데 글자로는 1개만 사용하기 때문에 나머지는 front 리스트에 추가
    else:
        front.append(item[0]*(item[1]//2)) # 반으로 나눴을 때 앞부분에 해당하는 리스트이므로 등장횟수 나누기 2만큼 리스트에 추가

front.sort() # 사전식으로 배열
back = front[::-1] # 좌우 반전해서 문자열 뒷부분
answer = front + center + back # 리스트 합치기
print(''.join(answer)) # 리스트 -> 문자열 변환
