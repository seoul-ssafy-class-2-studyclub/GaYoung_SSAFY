'''
[ 입력 ]
1. R(행), C(열), M(상어 수)
2. M개의 줄에 상어의 정보. (r, c): 상어의 위치, s: 속력, d: 이동방향, z: 크기
                                            d=1:위, d=2:아래, d3:오른쪽, 4:왼쪽
'''


'''
[ 문제 이해 ]
1. 상어는 최대 1마리
2. 상어는 크기, 속도 가지고있음.
3. 1초 동안 일어나는 일
    - 낚시왕 오른쪽으로 한칸 이동
    - 땅과 제일 가까운 상어 잡기(잡힌 상어는 사라짐)
    - 상어 이동 : 격자판의 경계 -> 방향 반대, 속력 유지
               : 이동 후 한칸에 상어 2마리 가능 -> 크기 큰 상어가 나머지 다 잡아먹음
'''

from heapq import heappop, heappush

R, C, M = map(int, input().split())
sharks = [[[] for _ in range(C + 1)] for _ in range(R + 1)]

for m in range(M):
    x, y, s, d, z = map(int, input().split())
    sharks[x][y] = [s, d, z]

# print(sharks)
total = 0  # 상어 크기의 합
person = 0
while True:
    person += 1
    if person > C:
        break

    if len(sharks) == 0:
        break

    shark_col = []

        # print(sharks)
        # 같은 줄에 있는 상어 잡기
        # 잡을 때, 같은 줄에 있는 상어가 있을 때, 하나면 그거 잡으면 됨
        # but, 여러개라면 그 중에 row가 작은 것을 택해야함
        if y == person:
            heappush(shark_col, (x, z))
            print(shark_col)

    # 잡을 상어가 있다면,
    # if len(shark_col) != 0:
    #     pass

    # 잡을 상어가 없다면, 상어 이동

