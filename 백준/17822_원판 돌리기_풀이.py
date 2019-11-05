'''
4 4 1
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
30

4 4 2
1 1 2 3
5 2 4 2
3 1 3 5
2 1 3 2
2 0 1
3 1 3
22
'''

'''
[풀이방법]
1. x 배수, d방향, k칸 : def move
   1-1. 배수 for m in range(M) 돌면서 x = mx
   1-2. 방향 0:시계방향, 1:반시계방향
   1-3. k칸 이동
2. 인접하면서 수가 같은 것을 모두 지우기 -> 수가 같으면 0으로 두기 : def same
   2-1. 세로로 같은 것은 board 세로로 보기
      2-1-1. board판을 넘어가면 안됨.
   2-2. 원둘레로 같은 것은 board 가로로 보기
      2-2-1. 왼쪽 오른쪽 모두 check
3. 큰 틀
    3-1. board있으면 for t in range(T):
                        move
                        same함수
'''


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
for t in range(T):
    x, d, k = map(int, input().split())
    for m in range(M):
