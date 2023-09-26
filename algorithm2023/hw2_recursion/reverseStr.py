def reverseStr(s):
    if len(s) == 1:
        return s
    else:
        return s[-1] + reverseStr(s[:-1])

t = int(input())
for _ in range(t):
    s = input()
    print(reverseStr(s))
