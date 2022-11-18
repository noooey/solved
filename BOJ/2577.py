n = 1
for i in range(3):
  n *= int(input())
num_list = list(str(n))

for i in range(10):
  print(num_list.count(str(i)))
