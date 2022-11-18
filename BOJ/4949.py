from collections import deque
import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break
    stack = deque([])
    for chr in string:
        if chr == '(':
            stack.append(')')
        if chr == '[':
            stack.append(']')
        if chr == ')' or chr == ']':
            if not stack:
                print('no')
                break
            elif stack.pop() != chr:
                print('no')
                break
        if chr == '.':
            if stack:
                print('no')
                break
            print('yes')
            break
