from copy import deepcopy

N = int(input())
board = []
for n in range(N):
    board.append(list(map(int, input().split())))
new_board = deepcopy(board)

mymax = 0
for x in range(N):
    for y in range(N):
        if mymax < board[x][y]:
            mymax = board[x][y]

queue = []
cnt_list = []
result_cnt = []
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
for k in range(1, mymax + 1):
    board = deepcopy(new_board)
    for i in range(N):
        for j in range(N):
            if board[i][j] <= k:  # k보다 작으면 0이라고 지정
                board[i][j] = 0
            elif board[i][j] > k:  # k보다 크면 모두 1이라고 지정
                board[i][j] = 1

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queue.append(i)
                queue.append(j)
                cnt = 1
                board[i][j] = 0
                while queue:
                    x = queue.pop(0)
                    y = queue.pop(0)
                    for a, b in near:
                        xi = x + a
                        yi = y + b
                        if 0 <= xi < N and 0 <= yi < N:
                            if board[xi][yi] != 0:
                                cnt += 1
                                queue.append(xi)
                                queue.append(yi)
                                board[xi][yi] = 0
                cnt_list.append(cnt)  # 안전한 영역의 크기 출력
                result_cnt.append(list(cnt_list))
# print(result_cnt)  # [[25], [25, 19], [25, 19, 2], [25, 19, 2, 3], [25, 19, 2, 3, 7], [25, 19, 2, 3, 7, 2], [25, 19, 2, 3, 7, 2, 2], [25, 19, 2, 3, 7, 2, 2, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1, 1, 3], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1, 1, 3, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1, 1, 3, 1, 1], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1, 1, 3, 1, 1, 2], [25, 19, 2, 3, 7, 2, 2, 1, 1, 7, 2, 2, 1, 1, 5, 2, 1, 1, 3, 1, 1, 2, 1]]

# <내가 원하는 것>
# k 가 1부터 board에 있는 최대값까지 돌때마다 cnt 저장
# ex. [[25],[19],[2,3,7,2],[2,1,1,7,2],[2,1,1,5,2],[1,1,3,6],[1,2],[1],[]]
# 이때 len이 제일 큰 것 -> 5개
print(len(result_cnt))
answer = [0] * len(result_cnt)
# for r in range(len(result_cnt)):
#     answer[r] = len(result_cnt[r])
# print(answer)