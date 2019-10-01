for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 1. 하나의 중심점에서 가로세로 값을 리스트에 넣고, 그 리스트들을 하나의 리스트에 넣기
    # 1-1. ls리스트에 중심점 마다의 필요한 값들 넣기
    #      (가로+세로-중심점 / 가로(-중심)+세로(-중심)+중심)
    # 1-2. 중심점 찾기 -> for x in , for y in ran
    # 1-3. 중심점 찾았을 때, for i in ra를 돌리면서 i != y일때 빼고 다 ls에 넣기
    # 1-4. 중심점 찾았을 때, for j in ra를 돌리면서 j != x일때 빼고 다 ls에 넣기
    # 1-5. 중심점마다 ls에 넣고, 초기화시키면서 ls_t에 넣기
    ls_t = []
    for x in range(N):
        for y in range(N):
            ls = []
            ls.append(board[x][y])
            for i in range(N):
                if i != y:  # 가로
                    ls.append(board[x][i])
            for j in range(N):
                if j != x:  # 세로
                    ls.append(board[j][y])
            ls_t.append(ls)

    # 2. 최소비용과 그에 따른 도로 높이 설정 (각각 ls에서 평균을 구하고 비용 min, 높이 min)
    # 2-1. 2.0<=mean<2.5이면 2, 2.5<=mean<3이면 3
    #     2-1-1. from math import round 하면 round(mean)하면 반올림
    #     2-1-2. 1.4*2=2.8=>2, 1.5*2=3.0=>3   ->   a = int(mean) + int(mean * 2) % 2 => 1.4이면 1 + 0, 1.5이면 1 + 1
    # 2-2. 도로 높이를 구했다면, 최소비용을 구해야함(ls마다 최소비용) -> rs
    # 2-3. 1) mymin vs rs  2) height vs a
    #     1) 1. mymin과 rs를 비교해 최소비용이 작은 것을 선택해야함
    #        2. mymin이 rs로 갱신될 때, 그 rs에 따른 height도 바뀌어야함(height = a)
    #     2) 1. 최소비용이 같으면 도로 높이가 낮은 것을 채택 -> mymin == rs 이면, height = a

    mymin = 99999  # rs
    height = 0  # a
    for i in ls_t:
        mean = sum(i)/len(i)  # 1.4
        a = int(mean) + int(mean * 2) % 2  # 1
        rs = 0
        for j in i:
            rs += abs(j - a)
        if mymin > rs:
            mymin = rs
            height = a
        elif mymin == rs:
            if height > a:
                height = a
    print(mymin, height)
