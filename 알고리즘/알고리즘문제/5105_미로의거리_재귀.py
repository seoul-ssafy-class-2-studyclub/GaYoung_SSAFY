def go(ls, dist=0):
    x, y = ls
    for dx, dy in near:
        if 0 <= x+dx < n and 0 <= y+dy < n:
            if vis[x+dx][y+dy] == 0:
                vis[x+dx][y+dy] = 1
                if bd[x+dx][y+dy] == 0:
                    a = go([x+dx, y+dy], dist+1)
                    if a[0] == 1:
                        return 1, a[1]
                    elif a[0] == 0:
                        return 0, 0
                elif bd[x+dx][y+dy] == 3:
                    return 1, dist
    return 0, 0

for T in range(int(input())):
    n = int(input())
    near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    bd = []
    vis =[]
    for i in range(n):
        bd.append([int(i) for i in input()])
        vis.append([0 for i in range(n)])
    for x in range(n):
        for y in range(n):
            if bd[x][y] == 2:
                start = [x, y]
    print(go(start)[1])