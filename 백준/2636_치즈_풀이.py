'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''

'''
[풀이방법]
1. 공기와 접촉된 치즈는 녹고, 0이지만 공기와 접촉하지 않은 치즈는 녹지 않음
2. 한바퀴 돌면서 녹으면 hour+=1
3. 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수 출력
'''

'''
내부 공기는 치즈에 영향을 주지 않는다!!!!
외부공기와 내부공기를 구분해야할듯하다.
외부공기를 모두 2로 두고, 내부공기는 0으로 두고 치즈는 1.
외부공기에 접하는 치즈는 2로 바꾸고 마지막 치즈 갯수 세기
'''

near = [(0, -1), (-1, 0), (1, 0), (0, 1)]

# 외부공기 모두 2로 만들기 -> 치즈 1, 내부공기 0
def air_out(x, y):
    for a, b in near:
        if 0 <= x + a < N and 0 <= y + b < M and cheeze[x + a][y + b] == 0:
            cheeze[x + a][y + b] = 2
            air_out(x + a, y + b)


# 외부공기와 접하는 치즈 녹이기
# 기준: 치즈1  (기준이 2면 안됨!!)
# 일단 치즈 1 사방에 2가 있다면 치즈1을 3으로 바꾸고, 다시 3을 2로 바꿈
def melt():
    for i in range(N):
        for j in range(M):
            for a, b in near:
                if 0 <= i + a < N and 0 <= j + b < M and cheeze[i + a][j + b] == 1:
                    if cheeze[i + a][j + b] == 2:
                        cheeze[i][j] = 3

    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 3:
                cheeze[i][j] = 2
    # return 1을 해서 시간이 몇시간 지나는지 check한다
    return 1


# 치즈(1)인 것 세는 함수로 치즈갯수 세기
def count_cheeze():
    for i in range(N):
        for j in range(M):
            cnt = 1
            if cheeze[i][j] == 1:
                cnt += 1
    return cnt


# 치즈 시작
N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

hour = -1
air_out(0, 0)
temp = []
cnt = 1

while cnt > 0:
    cnt = count_cheeze()
    temp.append(cnt)
    hour += melt()
    for i in range(N):
        for j in range(M):
            if cheeze[i][j] == 0:
                air_out(i, j)

print(temp)
print(hour)
'''
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
'''