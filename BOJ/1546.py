N = int(input())
num_list = list(map(int, input().split()))
M = max(num_list)

num_list = map(lambda x: x/M*100, num_list)

print(sum(num_list)/N)
