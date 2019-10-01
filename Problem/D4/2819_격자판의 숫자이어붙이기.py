# 1. 임의의 위치에서 시작
# 2. 동서남북 네 방향으로 인접한 격자
# 3. 총 6번 이동으로 7자리 숫자 생성
# 4. 한 번 거쳤던 격자칸을 다시 거쳐도 됨
# 5. 서로 다른 일곱 자리 수들의 개수 구하기

# 방법1
'''
string인 result를 list 안에 있으면 넣지 않고, list안에 없으면 넣음
'''
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(x, y, result, cnt):

    if cnt == 7:
        if result not in visit:
            visit.append(result)
            return

    else:
        for a, b in near:
            xi = x + a
            yi = y + b
            if 0 <= xi < 4 and 0 <= yi < 4:
                # result += board[xi][yi]
                dfs(xi, yi, result + board[xi][yi], cnt + 1)
# 이때, result += board[xi][yi]하고 dfs(xi, yi, result, cnt+1)하는 것이 아니라
# dfs(xi, yi, result + board[xi][yi], cnt + 1)라고 해야함
# why? 위에서 cnt == 7일때 result값을 빼는데, result값 자체를 바꿔주면서 dfs를 돌려야함.



for t in range(int(input())):
    board = [list(input().split()) for _ in range(4)]
    visit = []

    for i in range(4):
        for j in range(4):
            result = ''  # 계속 초기화
            result += board[i][j]
            dfs(i, j, result, 1)

    print('#{} {}'.format(t+1, len(visit)))


# 방법2
'''
visit라는 dictionary를 사용함.
'''
near = [[0, 1], [1, 0], [-1, 0], [0, -1]]
def go(x, y, st):
    if len(st) == 7:
        vis[st] = 1
        return
    for dx, dy in near:
        xi = x + dx
        yi = y + dy
        if 0 <= xi < 4 and 0 <= yi < 4:
            go(xi, yi, st + bd[xi][yi])


for t in range(int(input())):
    bd = [list(input().split()) for i in range(4)]
    vis = {}
    for x in range(4):
        for y in range(4):
            go(x, y, bd[x][y])
    print('#{}'.format(t + 1), len(vis))