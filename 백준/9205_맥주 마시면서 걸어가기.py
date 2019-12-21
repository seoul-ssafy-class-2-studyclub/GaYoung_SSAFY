'''맥주 한 박스에 20개. 50미터에 한병씩 마시려함
맥주를 더 구매해야할수도있음
편의점들리면 빈병을 버리고 새 맥주병을 살 수 있음
그치만 박스 안의 맥주는 20병을 넘을 수 없음

좌표: 상근이 집, 편의점, 페스티벌

2 : 테케
2 : 편의점개수
0 0 : 상근이집
1000 0 : 편의점
1000 1000 : 편의점
2000 2000 : 페스티벌
'''

'''
[로직]
집 - 편의점, 편의점 - 편의점, 편의점 - 페스티벌 거리가 모두 20*50=1000이면 happy
만약 하나라도 안된다면 sad
'''
'''
1
2
0 0
1000 0
1000 1000
2000 1000
'''
for t in range(int(input())):
    n = int(input())
    ls = []

    stop = False
    for i in range(n+2):
        ls.append(list(map(int, input().split())))

    for l in range(1, n+2):
        dis = abs(ls[l][0] - ls[l-1][0]) + abs(ls[l][1] - ls[l-1][1])

        if dis > 1000:
            stop = True
            break

    if stop:
        res = 'sad'
    else:
        res = 'happy'
    print(res)
