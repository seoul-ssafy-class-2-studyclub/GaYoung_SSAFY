# compute는 제공해주는 함수
user_input = list(map(int, input().split()))
# print(user_input)
# 1 1 3 4 3 6 3
answer = ''
data = {}
for i in user_input:
    if i in data:
        answer += str(data[i]) + ' '
    elif i not in data:
        data[i] = compute(i)
        answer += str(compute(i)) + ' '
print(answer[:-1])