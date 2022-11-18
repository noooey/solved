N = int(input())
lst = []
for i in range(N):
    lst.append(input())
str = ""
same = True
for i in range(len(lst[0])):
    for j in range(1, N):
        if lst[0][i] != lst[j][i]:
            same = False
            break
    if same == True:
        str += lst[0][i]
    else:
        str += "?"
        same = True

print(str)