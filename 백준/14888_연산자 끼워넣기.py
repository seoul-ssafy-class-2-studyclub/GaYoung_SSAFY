result = []
def per(arr):  # 순열
    if len(arr) == sum(word):
        result.append(arr)
        return result
    else:
        for idx in range(len(eq_t)):
            if visit[idx]:
                continue
            elif visit[idx] == False:
                visit[idx] = True
                per(arr + [eq_t[idx]])
                visit[idx] = False


N = int(input())
num = list(map(int, input().split()))
word = list(map(int, input().split()))
eq = ['+', '-', '*', '/']

eq_t = []
for i in range(4):
    eq_t += eq[i] * word[i]

for i in range(len(eq_t)):
    if eq_t[i] == '':
        eq_t.pop(i)  # ['+', '*']

visit = [False] * (len(eq_t) + 1)

per([])


answer = []
for i in result:
    rs_max = num[0]
#     # num2 = num[:]
    for j in range(len(i)):
        # print(i[j])
        if i[j] == '+':
            rs_max += num[j + 1]
        elif i[j] == '-':
            rs_max -= num[j + 1]
        elif i[j] == '*':
            rs_max *= num[j + 1]
        elif i[j] == '/':
            rs_max /= num[j + 1]
            rs_max = int(rs_max)


    answer.append(rs_max)

print(max(answer))
print(min(answer))
