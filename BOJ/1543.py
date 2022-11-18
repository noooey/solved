import sys
input = sys.stdin.readline

doc = ('').join(list(input())[:-1])
word = ('').join(list(input())[:-1])

doc = doc.replace(f'{word}', '*')

print(doc.count('*'))
