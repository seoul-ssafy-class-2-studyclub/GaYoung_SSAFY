board = [[12,15],[19,21]]  # 34
# board = [[3,6,8],[1,4,7],[2,1,4]]  # 15

n = len(board)
a, b, c = [False] * n, [False] * (2*n-1), [False] * (2*n-1)

def check(board, i):
    val = 0

    if i == n:
        return val

    for j in range(n):
        if not(a[j] or b[i+j] or c[i-j+n-1]):
            a[j] = b[i + j] = c[i - j + n - 1] = True
            val += board[i][j]
            check(board, i)
            a[j] = b[i + j] = c[i - j + n - 1] = False

def solution(board):
    answer = 0
    for i in range(n):
        print(check(board, i))
        if answer < check(board, i):
            answer = check(board, i)

    return answer

print(solution(board))