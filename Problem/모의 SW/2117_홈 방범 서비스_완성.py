for t in range(int(input())):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    houses = []
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:
                houses.append((x, y))

    earn = len(houses) * M  # 모든 집에서 수익을 얻었을 때, 운영 비용보단 커야한다. -> while 탈출 조건

    K = 1
    mymax_cnt = 0
    while True:
        fee = K ** 2 + (K-1) ** 2  # 운영비용
        # while 탈출조건
        if earn - fee < 0:
            break

        # True가 될때까지 도는 경우
        for i in range(N):
            for j in range(N):
                total = -fee  # 집이 있을 때마다 M을 더해주고 마지막에 fee를 빼서 양수가 나오면 회사는 이득인 것
                cnt = 0
                for house in houses:  # x,y축이 N을 돌면서 집을 기준으로 거리를 측정!!
                    # 0인 곳을 먼저 돌면 돌았던 곳도 돌게 되기 때문에 해도 상관 없지만, 굳이 할 필요없음
                    # 집을 기준으로 서비스 구역을 측정해라!
                    dis = abs(house[0] - i) + abs(house[1] - j)
                    if dis < K:  # 최종적으로 서비스가 이루어지는 지역은 가로 세로합쳐서 K미만인 지역!
                        total += M  # 특정 집이 서비스 지역 내에 있다면 cnt를 하나 올리고,
                        cnt += 1  # 집이 내는 가격(M)을 total(가격)에 더해주기
                if total >= 0 and mymax_cnt < cnt:  # total >= 0이어야 회사가 손해 안봄.
                    # 가장 많은 집들에 제공하는 서비스 영역을 찾아야하므로 mymax_cnt를 갱신해줌
                    profit = total
                    mymax_cnt = cnt
        K += 1

    print('#{} {}'.format(t+1, mymax_cnt))