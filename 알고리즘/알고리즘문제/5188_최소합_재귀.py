near = [(1, 0), (0, 1)]

def dfs(x, y, rs):
    global mn  # 밑에서 제시한 값을 함수안에서 변수 값을 변경할 때 사용!
    if x == N - 1 and y == N - 1:  # 탈출조건
        if mn > rs:
            mn = rs
        return 0
    elif rs > mn:
        return 0

    for a, b in near:
        xi = x + a
        yi = y + b
        if 0 <= xi < N and 0 <= yi < N:
            dfs(xi, yi, rs + board[xi][yi])  # 만약 3000번 이상이면 재귀X


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    start = board[0][0]
    mn = 9999
    dfs(0, 0, start)
    print('#{} {}'.format(t + 1, mn))
