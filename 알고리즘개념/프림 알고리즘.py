'''
[프림 알고리즘]

1. 개념
    : 한 정점에 연결된 간선들 중 한개씩 선택하면서 최소신장트리를 만들어가는 방식
2. 방법
    2-1. 임의 정점 선택
    2-2. 선택 노드의 인접노드 중 최소비용의 간선이 존재하는 정점 선택
    2-3. 모든 정점이 선택될 때까지 2-2반복
  * 이때, 상호배타집합(트리, 비트리) 정보필요
'''

# 알고리즘 동작과정
def MST_PRIM(G, s):  # G: 그래프, s: 시작정점

    key = [INF] * N    # 우리는 간선 중 최소값을 가지는 간선을 선택할 것이므로 가중치를 무한대로 초기화
    pi = [None] * N    # 트리에서 연결될 부모 정점을 저장 -> key의 최소 가중치로 연결할 수 있는 간선의 정점 정보 -> 정점, 부모정점 저장
    visited = [False] * N    # 방문여부 초기화
    key[s] = 0    # 시작 정점의 가중치를 0으로 설정

    for _ in range(N):   # 정점의 갯수만큼 반복
        min_idx = -1
        min = INF

        for i in range(N):    # 방문하지 않은 정점 중 key값이 최소인 정점 찾기
            if not visited[i] and key[i] < min:
                min = key[i]
                min_idx = i
        visited[min_idx] = True    # 최소 가중치 정점 방문처리

        for v, val in G[min_idx]:    # 선택 정점의 인접한 정점
            if not visited[v] and val < key[v]:   # 비트리의 정점중 key값보다 더 작은 값이 있다면
                key[v] = val    # 가중치 갱신 -> =트리 정점들과 연결하기 위해 필요한 최소 간선 비용을 의미
                pi[v] = min_idx    # 트리에서 연결된 부모 정점