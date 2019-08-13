def is_p(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1-i]:
            return False
    return word

for t in range(10):
    N = int(input())   # 찾아야하는 회문 길이 : N = 5
    board = [list(input()) for row in range(8)]  # [['C', 'B', 'C', 'A', 'B', 'B', 'A', 'C'], ['B..]]
    board2 = [[0] * 8 for _ in range(8)]
    cnt = 0

    # board2만들기
    for j in range(8):
        for i in range(8):
            board2[j][i] = board[i][j]

    # 가로 (board)
    for k in board:
        for l in range(8-N+1):
            word = k[l:l+N]
            data = is_p(word)
            if data != False:
                cnt += 1

    # 세로
    for k in board2:
        for l in range(8-N+1):
            word = k[l:l+N]
            data = is_p(word)
            if data != False:
                cnt += 1

    # 결과값
    print('#{} {}'.format(t+1, cnt))