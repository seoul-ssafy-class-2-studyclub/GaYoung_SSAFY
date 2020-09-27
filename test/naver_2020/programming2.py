blocks = [[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
# blocks = [[0, 92], [1, 20], [2, 11], [1, -81], [3, 98]]

n = len(blocks)
answer = []
for i in range(n):
    temp = [0]*(i+1)
    answer.append(temp)

for i in range(n):
    a, b = blocks[i]
    answer[i][a] = b


check = []
for i in range(n):
    for j in range(len(answer[i])):
        if answer[i][j] == 0:

            if j-1 >= 0:
                if answer[i-1][j-1] != 0 and answer[i][j-1] != 0:
                    answer[i][j] = answer[i-1][j-1] - answer[i][j-1]

            if j+1 < len(answer[i]):
                if answer[i-1][j] != 0 and answer[i][j+1] != 0:
                    answer[i][j] = answer[i-1][j] - answer[i][j+1]

            if answer[i][j] == 0:
                check.append([i, j])

# print(answer)
# if len(check) != 0:
check = sorted(check, reverse=True)
# print(check)
visit = [0] * len(check)
while True:
    if visit == [1] * len(check):
        break

    for l in range(len(check)):
        x, y = check[l]
        if y+1 < len(answer[x]):
            if answer[x-1][y] != 0 and answer[x][y+1] != 0 and visit[l] == 0:
                answer[x][y] = answer[x-1][y] - answer[x][y+1]
                print(answer[x][y])
                visit[l] = 1
            elif answer[x-1][y] == 0 and answer[x][y+1] != 0 and visit[l] == 0:
                answer[x][y] = answer[x-1][y] - answer[x][y+1]
                visit[l] = 1
                print(answer[x][y])
            elif answer[x-1][y] != 0 and answer[x][y+1] == 0 and visit[l] == 0:
                answer[x][y] = answer[x-1][y] - answer[x][y+1]
                visit[l] = 1
            # print(check)
            # print(visit)
print(answer)
#
# result = []
# for i in range(n):
#     for j in range(len(answer[i])):
#         result.append(answer[i][j])
#
# # print(answer)
#
# print(result)
