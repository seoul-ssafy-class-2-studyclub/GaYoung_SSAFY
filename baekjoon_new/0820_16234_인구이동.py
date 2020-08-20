'''
2 20 50
50 30
20 40

2 40 50
50 30
20 40

2 20 50
50 30
30 40

3 5 10
10 15 20
20 30 25
40 22 10

4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
'''

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

near = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def change():  # 인구의 평균으로 바꿔주는 함수
    return 0

def move():  # L ~ R인 곳을 나타내는 함수
    return 0

