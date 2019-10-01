near = [(0, -1), (-1, 0), (1, 0), (0, 1)]

for tc in range(int(input())):
    N = int(input())
    maze = []
    for n in range(N):
        maze.append(list(map(int, input())))

    start_index = False

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start_index = (y, x, 0)
                break
        if start_index:
            break

    result = 0
    stack = [start_index]
    while True:
        y, x, t = stack.pop()
        for dy, dx in near:
            ry = y + dy
            rx = x + dx
            if 0 <= ry < N and 0 <= rx < N:
                if not maze[ry][rx]:
                    maze[ry][rx] = 1
                    stack.append((ry, rx, t + 1))
                elif maze[ry][rx] == 3:
                    result = 1
                    break
        if result == 1:
            break

        if not stack:
            break
    if result == 0:
        t = 0
    print('#{} {}'.format(tc + 1, t))