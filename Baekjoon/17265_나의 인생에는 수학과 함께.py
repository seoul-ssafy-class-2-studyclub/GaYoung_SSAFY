near = [(1, 0), (0, 1)]
def dfs(x=0, y=0, result=0, cal=0):
    global mymin, mymax

    if cal == 0:
        result += int(board[x][y])
    elif cal == 1:
        result -= int(board[x][y])
    elif cal == 2:
        result *= int(board[x][y])
    # elif cal == 3:  # 숫자인 경우
    #     pass

    # 탈출 조건
    if x == N - 1 and y == N - 1:
        if mymax < result:
            mymax = result
            # return이 있으면 min으로 내려갈 수 없다. result=4,5,6,9이면 
            # return이 있다면 mymax=4, 5, 6, 9로 갱신되지만 mymin은 갱신되지 않음
        if mymin > result:
            mymin = result
            return
        
    for a, b in near:
        xi, yi = x + a, y + b
        if 0 <= xi < N and 0 <= yi < N:
            if board[x][y] == '+':
                dfs(xi, yi, result, 0)
            elif board[x][y] == '-':
                dfs(xi, yi, result, 1)
            elif board[x][y] == '*':
                dfs(xi, yi, result, 2)
            else:  # 문자가 아닌 숫자인 경우
                dfs(xi, yi, result, 3)

N = int(input())
board = [list(input().split()) for _ in range(N)]

mymax = -1e9
mymin = 1e9

dfs()
print(mymax, mymin)