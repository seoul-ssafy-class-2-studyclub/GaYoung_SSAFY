n, m = map(int, input().strip().split())

mat = [list(input()) for _ in range(n)]
DEBUG = False
chair = []
people = []


# 조건1 : 나보다 의자에 가까이 있는 사람이 보이면, 그 사람이 먼저 앉는다는 것을 알기 때문에 양보할 수밖에 없다.
# 조건2 : 하나의 'X' 문자와 같은 거리에 떨어진 'L'은 2개 이상 존재하지 않음이 보장된다.
# 즉, 어떤 의자에 앉는 사람은 다른 어떤 사람보다 의자와의 거리가 가까운 것이 보장되어 있음

# 0 부터 (0,0),(n-1,m-1)까지의 거리 모든 경우의 수 뽑기 == 최대 2만개
# 왜? 의자와 사람의 거리가 가장 짧은 순으로 보면서 지울거니까
short_cut = [{} for _ in range(n**2+m**2)]
for i in range(n):
    for j in range(m):

        if mat[i][j] == 'X':
            people.append((i, j))
        if mat[i][j] == 'L':
            chair.append((i, j))

cnt = 0

# visited 용도 : 한 번 사용된 의자와 그 의자에 앉는(혹은 싸운) 사람들은 다시 보지 않도록 체크할 용도
visited = [[0] * m for _ in range(n)]

for x, y in people:
    for i, j in chair:
        # 거리기준으로 for문을 돌거기 때문에 거리를 인덱스로 만든 short_cut 리스트에 dict를 채운다.
        dis = (x-i) ** 2 + (y-j) ** 2
        if short_cut[dis].get((i,j)) == None:
            # i,j는 의자의 좌표, x, y는 사람의 좌표
            # 의자에 키값을 주는 이유는 사람을 키값으로 주면 2개의 의자가 나올 수 없으므로,
            # 의자에 키값을 부여해서 한 의자에 한사람, 혹은 두사람이 않도록 설계
            # 중복으로 보기때문에 일단은 한 의자에 두 명 이상의 사람이 앉을 수 있게된다.
            # 추후 거리순으로 탐색하면서 한 의자에
            short_cut[dis][(i,j)] = [(x, y)]
        else:
            short_cut[dis][(i,j)].append((x,y))

if DEBUG:
    print(short_cut)

    print(len(short_cut))

for dic in short_cut:
    if len(dic):
        for key, values in dic.items():
            if DEBUG:
                print(key, values)
                for a in visited:
                    print(a)
                print(cnt)
            if visited[key[0]][key[1]]:
                continue

            flag = 0
            for xx, yy in values:
                if visited[xx][yy]:
                    continue
                flag += 1
                visited[xx][yy] = 1

            # 플래그가 존재할때만 의자비짓티드를 체크하는 이유는
            # 사람과 의자가 한큐에 지워져야하므로 사람이 하나라도 지워졌을때만
            # 의자도 지워져야하고, 반대로 사람이 한번도 지워지지않는 구간에서는
            # 의자도 또한 지워지면 안되기때문
            if flag:
                visited[key[0]][key[1]] = 1

            if flag >= 2:
                cnt += 1
print(cnt)