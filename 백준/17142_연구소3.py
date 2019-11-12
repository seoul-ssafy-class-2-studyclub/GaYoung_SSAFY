'''
7 3
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
5
'''

'''
[풀이방법]
1. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 칸
2. N, M = 가로/세로, 바이러스 갯수
3. 여러개 2 중에서 M개 선택 -> 조합!
4. 바이러스 위치가 결정되면, bfs돌리면서 몇초만에 퍼뜨리는지 check
5. 최소시간 구하기
6. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력
'''

# 연구소2와 유사 -> 시간차이?

# 바이러스 가능한 경우
result = []
def virus(arr, k):
    if len(arr) == M:
        result.append(arr)
        return result
    else:
        for idx in range(k + 1, len(can_virus)):
            virus(arr + [can_virus[idx]], idx)

def spread(safe, q, cnt=0):
    while q:
        cnt += 1
        for _ in range(len(q)):
            x, y = q.pop(0)
            for a, b in near:
                xi, yi = (x + a, y + b)
                if 0 <= xi < N and 0 <= yi < N:
                    if new_board[xi][yi] == 0:
                        new_board[xi][yi] = 1
                        safe -= 1
                        q.append((xi, yi))
    return cnt, safe

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
near = [(-1, 0), (1, 0), (0, 1), (0, -1)]
safe = N * N - M

can_virus = []
virus_cnt = 0
# 바이러스 가능한 칸 찾기
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            can_virus.append([i, j])
            board[i][j] = '*'
            virus_cnt += 1
        elif board[i][j] == 1:
            safe -= 1

virus([], -1)

ls = []
mymin = 9999
for r in result:
    q = r[:]  # q를 deepcopy하지 않으면, r도 바뀌므로 바이러스가 여러개인 경우에 q에서 빈칸이 되면,
              # r도 빈칸이 되어 밑에 for문에서 에러가 뜬다.
    new_board = [row[:] for row in board]  # deepcopy해줘야 다음 조합으로도 board사용 가능
    # print(q)
for m in range(M):
    a = r[m][0]
    b = r[m][1]
    new_board[a][b] = '**'

    c, s = spread(safe, q)
    print(c, s)

    if s == (virus_cnt - M):
        ls.append(c)

if len(ls) == 0:
    print(-1)
else:
    print(min(ls))

