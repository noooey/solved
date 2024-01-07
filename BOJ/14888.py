# 시간초광~

from itertools import permutations
import sys
input = sys.stdin.readline

def calculate(num_arr, opt_arr):
    eval_str = str(num_arr[0])
    for i in range(len(opt_arr)):
        eval_str += opt_arr[i]
        eval_str += str(num_arr[i+1])
        eval_str = str(int(eval(eval_str)))
    return int(eval_str)

N = int(input())
num_arr = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))
# + - * %
operator = []
for _ in range(operator_cnt[0]):
    operator.append('+')
for _ in range(operator_cnt[1]):
    operator.append('-')
for _ in range(operator_cnt[2]):
    operator.append('*')
for _ in range(operator_cnt[3]):
    operator.append('/')

max_value = -float('inf')
min_value = float('inf')

for opt_arr in set(permutations(operator, len(operator))):
    cur_value = calculate(num_arr, opt_arr)
    max_value = max(max_value, cur_value)
    min_value = min(min_value, cur_value)

print(max_value)
print(min_value)
