'''
[ 풀이방법 ]
1. 궁수배열 -> combination
2. 조합 별로 적 쏘기
   2-1. 거리가 D이하인 궁수
   2-2. 적이 여럿이면 가장 왼쪽 적 공격
3. 적 이동
   3-1. board판 나가면 게임에서 제외됨
4. 모든 적이 격자판에서 제외되면 게임 끝!
'''

from itertools import combinations

def game(row, c1, c2, c3):
    global kill

    q = set()
    for col in [c1, c2, c3]:
        flag = False
        for d in range(1, D + 1):  # D거리 이하에있는 적을 잡겠다
            for c in range(-d+1, d):  # 왜 c랑 r순서를 바꾸면 28퍼에서 실패하는거지?
                for r in range(1, d + 1):
                    if r + abs(c) == d:
                        xi, yi = row - r, col + c
                        if 0 <= xi and 0 <= yi < M:
                            if board_n[xi][yi] == 1:
                                q.add((xi, yi))
                                flag = True
                                break

                if flag:
                    break
            if flag:
                break

    for a, b in list(q):
        board_n[a][b] = 0
        kill += 1


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

can_shooter = [m for m in range(M)]
shooter = list(combinations(can_shooter, 3))

mymax = 0
for shot in shooter:
    board_n = [b[:] for b in board]
    y1, y2, y3 = shot

    kill = 0
    x = N
    while x >= 0:  # 한바퀴 돌때마다 x를 줄임 (board판을 한줄씩 위로 보냄)
        game(x, y1, y2, y3)
        x -= 1

    if mymax < kill:
        mymax = kill

print(mymax)