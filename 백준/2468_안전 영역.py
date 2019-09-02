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
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
for k in range(mymax + 1):
    board = deepcopy(new_board)
    for i in range(N):
        for j in range(N):
            if board[i][j] <= k:  # k보다 작으면 0이라고 지정
                board[i][j] = 0
            elif board[i][j] > k:  # k보다 크면 모두 1이라고 지정
                board[i][j] = 1
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queue.append(i)
                queue.append(j)
                cnt += 1
                board[i][j] = 0
                while queue:
                    x = queue.pop(0)
                    y = queue.pop(0)
                    for a, b in near:
                        xi = x + a
                        yi = y + b
                        if 0 <= xi < N and 0 <= yi < N:
                            if board[xi][yi] != 0:
                                queue.append(xi)
                                queue.append(yi)
                                board[xi][yi] = 0
    cnt_list.append(cnt)  # 안전한 영역의 크기 출력

# <내가 원하던 것>
# k 가 1부터 board에 있는 최대값까지 돌때마다 cnt 저장
# ex. [[25],[19],[2,3,7,2],[2,1,1,7,2],[2,1,1,5,2],[1,1,3,6],[1,2],[1],[]]
# 이때 len이 제일 큰 것 -> 5개

# <내가 구현해낸 것>
print(max(cnt_list))  # [1, 1, 4, 5, 5, 4, 2, 1, 0]
# board[i][j] == 1일 때 cnt += 1을 해준 것은 새로운 안전영역에 갈때마다 += 1을 해준 것이므로 영역의 갯수를 바로 알 수 있음
# k가 1부터 board의 최대값일때까지의 영역갯수 -> max하면 정답!