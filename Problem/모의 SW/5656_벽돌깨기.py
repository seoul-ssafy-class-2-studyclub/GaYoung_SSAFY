for t in range(int(uinput())):
    N, W, H = map(int, input().split())
    brick = []
    for h in range(H):
        brick.append(list(map(int, input().split())))