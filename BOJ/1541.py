import sys
input = sys.stdin.readline

def solutions(E):
    # 모든 조합 경우의 수에 대해 최솟값 산출
    list = []
    tmp = ''
    tmp_n = ''
    for e in E:
        if e == '-':
            tmp += str(int(tmp_n))
            list.append(eval(tmp))
            tmp_n = ''
            tmp = ''
        else:
            if e != '+':
                tmp_n += e
            else:
                tmp += str(int(tmp_n))
                tmp += e
                tmp_n = ''
    tmp += str(int(tmp_n))
    list.append(eval(tmp))

    answer = sys.maxsize
    for per in list:
        v = per - (sum(list)-per)
        answer = min(answer, v)
        print(answer)

    return answer

if __name__ == "__main__":
    equation = input().rstrip()
    print(solutions(equation))
