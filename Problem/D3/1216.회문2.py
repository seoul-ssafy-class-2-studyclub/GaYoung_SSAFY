def is_p(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1-i]:
            return False
    return len(word)

def longest_p(board):
    result = []
    for row in board:
        for t_v in range(2, len(board)):
            for x in range(len(board) - t_v + 1):
                word = is_p(row[x:x+t_v])
                result += [word]
    return max(result)

for t in range(10):
    N = int(input())
    board = [list(input()) for row in range(100)]
    board2 = [[0] * 100 for _ in range(100)]

    # board2 만들기
    for j in range(100):
        for i in range(100):
            board2[j][i] = board[i][j]

    data = [longest_p(board), longest_p(board2)]
    print('#{} {}'.format(N, max(data)))
