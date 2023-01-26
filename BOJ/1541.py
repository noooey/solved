import sys
input = sys.stdin.readline

def solutions(E):
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

    return list[0] - sum(list[1:])

if __name__ == "__main__":
    equation = input().rstrip()
    print(solutions(equation))
