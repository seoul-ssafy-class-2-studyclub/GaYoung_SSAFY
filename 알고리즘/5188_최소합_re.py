for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    total = []
    near = [(1, 0), (0, 1)]
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

    print(total)