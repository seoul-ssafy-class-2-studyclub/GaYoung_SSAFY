# TSP문제 -> 순열을 나열해서 다 조사하기!

def cart():



for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split()))]
    visit = [True] + [False] * (N - 1)

    mymin = 9999999999
    for i in range(N):
        for j in range(N):
            if board[0][j] != 0:
                result = board[0][j]
                visit[j] = True
                if j == i:

