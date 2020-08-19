'''
3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''

from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))
calcu = list(map(int, input().split()))
eq = ['+', '-', '*', '/']

eq_t = []
for i in range(4):
    eq_t += eq[i] * calcu[i]

mymax = 0
mymin = 999999999999999999999999999999999

result = list(permutations(eq_t, N-1))
# print(result[68])
answer = []
for i in result:
    res = numbers[0]

    for j in range(len(i)):
        if i[j] == '+':
            res += numbers[j + 1]

        elif i[j] == '-':
            res -= numbers[j + 1]

        elif i[j] == '*':
            res *= numbers[j + 1]

        elif i[j] == '/':
            res /= numbers[j + 1]
            res = int(res)
    answer.append(res)

print(max(answer))
print(min(answer))
