# m = 4
# n = 5
# board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']

m = 6
n = 6
board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']

'''
지워지는거 check -> visit사용 -> bd돌면서 지워지는거를 visit에 표시하고 한번에 0으로 바꾸기
bd = [['C', 'C', 'B', 'D', 'E'], 
      ['A', 'A', 'A', 'D', 'E'],
      ['A', 'A', 'A', 'B', 'F'], 
      ['C', 'C', 'B', 'B', 'F']]

visit = [[1, 0], [1, 1], [2, 0], [2, 1], [1, 2], [2, 2]]

visit 돌면서 bd[1][0] = 0으로 만들기

빈공간 채우기
'''

def same_friends(m, n, bd):
    visit = [[0] * n for _ in range(m)]

    for i in range(m-1):
        for j in range(n-1):
            word = bd[i][j]
            if word != 0 and word == bd[i][j+1] and word == bd[i+1][j] and word == bd[i+1][j+1]:
                visit[i][j] = 1
                visit[i][j+1] = 1
                visit[i+1][j] = 1
                visit[i+1][j+1] = 1

    for i in range(m):
        for j in range(n):
            if visit[i][j] == 1:
                bd[i][j] = 0

    return bd


def count_zero(m, n, arr):
    cnt = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1

    return cnt


def down(m, n, bbd):
    for k in range(n):
        for a in range(m-1, 0, -1):
            if bbd[a][k] == 0:
                for b in range(a-1, -1, -1):
                    if bbd[b][k] != 0:
                        bbd[a][k], bbd[b][k] = bbd[b][k], bbd[a][k]
                        break

                else:
                    break
    return bbd


def solution(m, n, board):
    bd = [list(i) for i in board]

    answer = 0
    before_cnt = 0

    while True:
        bbd = same_friends(m, n, bd)  # 같은애 지우기
        bdbd = down(m, n, bbd)  # 내리기
        zero = count_zero(m,n, bdbd)

        if zero == before_cnt:
            break
        else:
            answer = zero
            before_cnt = zero

        bd = bdbd

    return answer

print(solution(m, n, board))

