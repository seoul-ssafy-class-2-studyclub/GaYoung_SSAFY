data = list(input().split())
N = int(input())

visit = [False] * (len(data) + 1)
result = []
def permutation(arr):
    if len(arr) == len(data):  # 만약 data갯수만큼 하나하나 1~4개까지 하고싶다면, for문 돌리기!
        result.append(arr)
        return result
    else:
        for idx in range(len(data)):
            if visit[idx]:
                continue
            elif visit[idx] == False:
                visit[idx] = True
                permutation(arr + [data[idx]])
                visit[idx] = False  # 전 단계의 visit만 초기화

permutation([])
answer = sorted(result)
for i in range(len(answer)):
    if i == N - 1:
        rs = answer[i]

for i in rs:
    print(i, end='')
# print(answer)