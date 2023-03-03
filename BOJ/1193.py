x = int(input())

i = 1

while i < x:
    x -= i
    i += 1

if i % 2 == 0: # up
    print(f'{x}/{i+1-x}')
else: # down
    print(f'{i+1-x}/{x}')
