for t in range(int(input())):
    N, K = map(int, input().split())
    board = []
    count = 0
    for n in range(N):
        board.append(list(map(str, input().split())))
    board_re = list(map(list, zip(*board)))
    # print(board_re)

    for i in board:   # i = [0, 1, 0, 0, 1], [0, 1, 0, 1, 1],,,
        data = ''.join(i).split('0')
        count += data.count('1' * K)

    for j in board_re:
        data = ''.join(j).split('0')
        count += data.count('1' * K)
    print('#{0} {1}'.format(t+1, count))
