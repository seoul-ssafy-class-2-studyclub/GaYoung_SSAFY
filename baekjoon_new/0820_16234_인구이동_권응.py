import sys
sys.setrecursionlimit(10000)

near = [[-1,0],[0,1],[1,0],[0,-1]]

def go(x,y):
    global rs
    rs += bd[x][y]
    vis[x][y] = cnt
    dp[cnt].append([x,y])
    for a,b in near:
        xi,yi = a+x,b+y
        if 0 <= xi < n and 0 <= yi < n:
            if vis[xi][yi] == -1:
                dt = abs(bd[xi][yi] - bd[x][y])
                if l <= dt <= r:
                    go(xi,yi)


n,l,r = map(int, input().split())
bd = [list(map(int,input().split())) for i in range(n)]
dp_val = [0]*(n**2)
get_change = 0
while True:
    dp = [[] for i in range(n**2)]
    cnt = 0
    vis = [[-1]*n for i in range(n)]
    for x in range(n):
        for y in range(n):
            if vis[x][y] == -1:
                rs = 0
                go(x,y)
                dp_val[cnt]=rs
                cnt += 1
    if cnt == n**2:
        break
    for i in range(cnt):
        rs = dp_val[i]//len(dp[i])
        for x,y in dp[i]:
            bd[x][y] = rs
    get_change += 1

print(get_change)