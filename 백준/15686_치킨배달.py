import copy

#-----------------------------------------------------------------------
# 치킨집 고르는 방법 -> 조합으로 고르기
result = []
def is_chicken(arr, k):
    if len(arr) == M:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(chicken)):
            is_chicken(arr + [chicken[idx]], idx)

# is_chicken([], -1)
# print(result)  # [[[0, 1], [3, 0]], [[0, 1], [4, 0]],,,]
# -----------------------------------------------------------------------

N, M = map(int, input().split())
board = []
for n in range(N):
    board.append(list(map(int, input().split())))
new_board = copy.deepcopy(board)

# 치킨집, 일반 집인 곳 모두 찾기
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            chicken.append([i, j])
        elif board[i][j] == 1:
            house.append([i, j])
print(chicken)
is_chicken([], -1)  # 치킨집 가능 조합 모두 있는 list

# 치킨집이 선정되었다면 각각의 집 별로 치킨집의 거리를 구한다.
# 집 별로 치킨집과의 거리 중에, 더 짧은 거리인 곳을 택하고
# 그 값을 더하면 치킨집이 선정될 때마다 집과의 거리가 나온다.
# 어떤 치킨집이 선정되냐에 따라 최솟값을 구한다.

rs_d = []

######<배운 것>######
# for문 돌릴 때, 어떤 것을 기준으로 잡고 돌려야하는지 확인 -> 기준이 되는 것이 for문 위로 간다.

# flag 사용할 때, stop시킬 for문 바로 위에 작성

# mymin 사용할 때에는 나오지 않을 가장 큰 값을 설정해두고 점차 작아지게 하기!
# 어떤 for문을 돌 때 mymin 값이 갱신되며, 처음 값에서 다시 mymin해줘야하는지 알고, 그 for문 위에 mymin 초기화

for i in result:  # 치킨집 조합
    rs = 0
    for k in house:  # 집 갯수
        x = k[0]
        y = k[1]
        mymin = 1000
        for j in i:  # 치킨집 위치
            a, b = [j[0], j[1]]
            res = abs(a - x) + abs(b - y)
            if mymin > res:
                mymin = res
        rs += mymin
    rs_d += [rs]
    # print(rs, i)

    ######<배운 것>######
    # 디버깅할 때 내가 어떤 부분이 잘못되었는지 확인하기 위해서 필요한 값들을 따로 print하기!
    # run시켰을 때, error가 나면 에러나기 바로 직전까지 디버깅이 되는 것임

print(min(rs_d))
