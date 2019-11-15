import itertools

N = int(input())
number = list(map(int, input().split()))
eq = list(map(int, input().split()))
cal = ['+', '-', '*', '//']

total_cal = []
for i in range(4):
    total_cal += eq[i] * cal[i]

result = list(itertools.permutations(total_cal))
# print(result)  # [('+', '*'), ('*', '+')]

max_value = -1000000000
min_value = 1000000000

for r in result:
    total = number[0]
    for i in range()
