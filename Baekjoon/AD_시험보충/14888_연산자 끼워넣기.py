import itertools

N = int(input())
number = list(map(int, input().split()))
eq = list(map(int, input().split()))
cal = ['+', '-', '*', '/']

eq_t = []
for i in range(4):
    while eq[i] > 0:
        eq_t.append(cal[i])
        eq[i] -= 1


result = list(itertools.permutations(eq_t))
# print(result)  # [('+', '*'), ('*', '+')]

mymax = -1000000000
mymin = 1000000000

for r in result:
    total = number[0]
    for i in range(N - 1):
        calculate = r[i]
        if calculate == '+':
            total += number[i + 1]
        elif calculate == '-':
            total -= number[i + 1]
        elif calculate == '*':
            total *= number[i + 1]
        elif calculate == '/':
            total = int(total / number[i + 1])

    if mymax < total:
        mymax = total
    if mymin > total:
        mymin = total

print(mymax)
print(mymin)

