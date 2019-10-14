'''
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
'''


def drop():  # 버블이 터지면 위에있는 버블이 밑으로 내려오게 하기 위한 함수!
    for r in range(11, -1, -1):
        for c in range(6):
            row = r
            while row >= 0:
                if board[row][c] != '.':
                    board[r][c], board[row][c] = board[row][c], board[r][c]
                    break
                row -= 1


board = [list(input()) for _ in range(12)]
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]



stack = []


cnt = 0
flag = True
while flag:
    flag = False
    for i in range(12):
        for j in range(6):
            word = []  # 같은 단어 갯수가 4개 이상인지 확인하려고 만든 리스트
                       # 단어가 새로워질때, 초기화해줘야함.
            if board[i][j] != '.':
                stack.append((i, j))
                word.append((i, j))
                while stack:
                    x, y = stack.pop()
                    for a, b in near:
                        xi, yi = (x + a, y + b)
                        if 0 <= xi < 12 and 0 <= yi < 6:
                            if board[xi][yi] == board[x][y] and (xi, yi) not in word:
                                word.append((xi, yi))
                                stack.append((xi, yi))

                # word >= 4일 때, 단어를 .으로 바꾸고, 여러개 연쇄되어도 cnt는 한번 +=1 됨.
                # 여러 단어가 .으로 바뀐 다음에 cnt+= 1이 되어야하므로 flag = 1로 바꿈
                if len(word) >= 4:
                    flag = True
                    for w, o in word:
                        board[w][o] = '.'

    # x, y를 모두 돌았을 때, flag = 1이면 cnt += 1하고 drop하기
    if flag:
        cnt += 1

    drop()
# 한번 flag해서 drop사용했으면, 바뀐 보드에서 for i, for j 돌아서 확인해야함.
# 이때, 언제멈추냐. ->


print(cnt)
