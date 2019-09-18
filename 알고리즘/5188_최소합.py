for t in range(int(input())):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))
    # visit = [[False] * N for _ in range(N)]
    # visit 필요없다!!! why? 오른쪽이나 아래로만 가기때문에 갔던 길을 다시 가지 않음!!!!!

    near = [(1, 0), (0, 1)]
    total = []
    rs = board[0][0]
    stack = [(0, 0, rs)]

    while stack:
        x, y, result = stack.pop()
        if x == N - 1 and y == N - 1:
            total.append(result)
        for a, b in near:
            xi, yi = (x + a, y + b)
            if 0 <= xi < N and 0 <= yi < N:
                stack.append((xi, yi, result + board[xi][yi]))


    print('#{} {}'.format(t + 1, total))
