"""
abcd...z
0123...9
' '
<> -> x
"""

string = input().rstrip()

answer = ''
tmp = ''
reverse = True

i = 0
while i < len(string):
    if string[i] == '<':
        tmp = ''
        while string[i] != '>':
            tmp += string[i]
            i += 1
        answer += tmp
        answer += '>'
        i += 1
    else:
        tmp = ''
        while string[i] != ' ' and string[i] != '<':
            tmp += string[i]
            i += 1
            if i >= len(string):
                break
        answer += tmp[::-1]
        if i < len(string):
            if string[i] == ' ':
                answer += ' '
                i += 1

print(answer)
