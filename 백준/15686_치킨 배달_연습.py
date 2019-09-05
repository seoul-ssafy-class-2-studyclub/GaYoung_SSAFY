import copy
from pprint import pprint

N, M = map(int, input().split())
board = []
for n in range(N):
    board.append(list(map(int, input().split())))

result = []
def is_chicken(arr, k):
    if len(arr) == M:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(chicken)):
            is_chicken(arr + [chicken[idx]], idx)


chicken = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i, j])
        elif board[i][j] == 1:
            house.append([i, j])

# print(house)  # [[0, 3], [1, 0], [1, 2], [3, 3], [3, 4], [4, 3]]

is_chicken([], -1)
# print(result)  # [[[0, 1], [3, 0]], [[0, 1], [4, 0]],,, ]

res_t = []

for i in result:  # 조합
    rs = 0
    for k in house:  # 5개의 집
        x = k[0]
        y = k[1]
        for j in range(M):  # 치킨집갯수
            a = i[j][0]
            b = i[j][1]
            res = abs(a - x) + abs(b - y)
        rs += res
    res_t.append(rs)
print(res_t)
# print(min(res_t))
# print(res_t)  # [1, 2, 3, 4, 5, 2, 1, 2, 3, 4, 3, 2, 1, 2, 3, 4, 3, 2, 1, 2, 5, 4, 3, 2, 1]
# answer = []
# for l in range(0, len(res_t), len(house)):
#     ans = res_t[l:l + len(house)]
#     answer.append(sum(ans))
# print(min(answer))


# res = 0
# x = 0
# y = 3
# i = [[0, 1], [4, 4]]
# for j in range(M):
#     a = i[j][0]
#     b = i[j][1]
#     res = abs(a - x) + abs(b - y)
#     res_t.append(res)
# res_tt += [min(res_t)]
# print(res_tt)
    # pprint(new_board)
