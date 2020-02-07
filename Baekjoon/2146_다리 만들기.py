'''
1. 섬을 표시하기
   1-1.먼저 입력받은 맵에서 붙어있는 육지를 찾아 섬으로 묶기(DFS) -> 인접한 육지를 이동하면서 방문체크, 섬 갯수 카운트 +=1

2. 섬과 섬 사이의 거리를 BFS로 구하기
   2-1.섬과 섬 사이를 BFS를 통해 이동
   2-2.섬 아닌 곳을 이동하다가, 출발한 섬과 다른 섬을 만나면, 이동거리를 최솟값으로 업데이트한다.
'''

N = int(input())
earth = [list(map(int, input().split())) for _ in range(N)]

visit = [[False] * N for _ in range(N)]
