import sys
input = sys.stdin.readline

nums = []

for i in range(2, 10001):
    sosu = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            sosu = False
            break
    if sosu:
        nums.append(i)

def solutions(n):
    if n == 4:
        return print(2, 2)
    a = int(n/2)
    b = int(n/2)
    while True:
        if a%2 != 0:
            if a in nums and b in nums:
                return print(a, b)
            else:
                a -= 2
                b += 2
        else:
            a -= 1
            b += 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        solutions(int(input()))
