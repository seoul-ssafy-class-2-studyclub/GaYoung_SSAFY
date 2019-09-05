N, M = map(int, input().split())
board = []
for n in range(N):
    board.append(list(map(int, input().split())))
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
cnt_board = [[0] * M for _ in range(N)]
new_cnt_board = [row[:] for row in cnt_board]

ice_list = []
year = 0
while len(ice_list) < 2:

# board에서 각 칸마다 주변 사방면이 0인거 갯수 세기
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for a, b in near:
                    # 꼭 while문 쓸 필요는 없다!!
                    # (1, 1)에서 0인 것들을 확인하고 cnt_board에 cnt 값을 넣어준 다음에 (1, 2)로 간다.
                    # (1, 2)의 값이 0이 아니면 방금 한 과정 반복, 0이면 pass
                    xi, yi = (i + a, j + b)
                    if 0 <= xi < N and 0 <= yi < M and board[xi][yi] == 0:
                        cnt += 1
                cnt_board[i][j] = cnt
    # pprint(board)
    # pprint(cnt_board)
    # print(ice_cnt)
    '''
    [[0, 0, 0, 0, 0, 0, 0],
     [0, 2, 2, 1, 2, 0, 0],
     [0, 2, 0, 1, 0, 3, 0],
     [0, 2, 2, 1, 2, 0, 0],
     [0, 0, 0, 0, 0, 0, 0]]
    '''
    # pprint(board)

    # board에 cnt_board의 값 빼주기(=빙산 녹음) -> cnt_board 초기화 해주기
    for i in range(N):
        for j in range(M):
            # print(board[i][j], cnt_board[i][j])
            board[i][j] -= cnt_board[i][j]
            if board[i][j] < 0:
                board[i][j] = 0
            cnt_board[i][j] = 0
    # pprint(board)
    ice_list = []
    # board에서 빙산 갯수 새기
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and cnt_board[i][j] != 1:
                ice_cnt = 1
                cnt_board[i][j] = 1
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < N and 0 <= yi < M and cnt_board[xi][yi] == 0 and board[xi][yi] != 0:
                            cnt_board[xi][yi] = 1
                            queue.append((xi, yi))
                            ice_cnt += 1
                ice_list.append(ice_cnt)
                # print(i, j)
                # print(ice_list)
                cnt_board[i][j] = 0
            # print(len(ice_list))
    year += 1
    # print('----------------------------------------')
print(year)