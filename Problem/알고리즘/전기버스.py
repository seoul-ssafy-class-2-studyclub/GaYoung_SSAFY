for t in range(int(input())):
    K, N, M = list(map(int, input().split()))
# K = 최대 이동가능거리, N = 총마지막정류장수, M = 충전기 설치 정류장
    data = list(map(int, input().split()))
    station = 0  # 버스의 현재 위치
    count = 0  # 충전기 정류장에 몇번 섰나
    data.append(N)  # 충전기 설치되어있지 않은 마지막 정류장을 포함시켜야 거기서 멈출 수 있음
    back = 0  # K칸씩 이동했을 때, 그 곳에 정류장이 없다면 정류장을 찾으러 뒤로 돌아가야함

    for kilo in range(N+1):  # kilo가 n에 갈때까지 가는거리
        # print(kilo, station)
        if station == N:  # station이 마지막정류장이면 멈춘다 
            break         # why? 멈추지 않으면 9 -> 12로가고 계속 count가 세짐
        elif station != 0:  #이 조건을 쓰지 않으면 station이 else문으로 빠져서 -1이 나오게되면 계속 else 문으로만 감
            if station in data:  # station이 0이 아닐 때, station이 충전기설치되어있는 곳에가면
                station += K  # 위치를 이동시켜주고
                count += 1  # 횟수도 더하고
                back = 0  # 이때 뒤로가는 것을 초기화시킴. why? 초기화안시키면 한번 K번 가고 새로 K번 가려하면 back은 0이 되어야함.
            else:
                station -= 1  # station이 데이터에 없으면 한칸씩 뒤로간다
                back += 1  # 뒤로가는 것을 하나씩 더해서 
                if back == K:  # 만약 back이 K만큼 이동해서 원래 자리로 돌아온다면
                    count = 0  #count를 0으로 초기화시킨다.
                    break  # break를 해줘야 count가 0으로 남아있음
        else:  # station이 0이면 (처음출발지) K만큼 일단 먼저 가야함
            station += K

    print('#{0} {1}'.format(t+1, count))

''' 
if station == N:
    break
안넣으면 10넘어서도 계속 더해짐
3 10 5
1 3 5 7 9
3 0
6 1
5 1
8 2
7 2
10 3
13 4
12 4
11 4
10 4
13 5
'''
