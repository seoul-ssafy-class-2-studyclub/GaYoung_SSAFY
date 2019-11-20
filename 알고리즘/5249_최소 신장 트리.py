'''
최소신장트리 : 무향!!!

0 1 1
1 0 6
1 6 0
이렇게 표현하기 위해! -> 무향이므로 양방향 다 표시해줘야해서
   1. w_list를 보드판으로 만든다
   2. w_list[node1][node2] = w
      w_list[node2][node1] = w 이렇게 양방향 다 표시해야함
'''

'''
[최소신장트리]
1. 선택 노드 외의 인접노드 중 최소비용의 간선이 존재하는 정점 선택
    -> 예시그림 확인!!!
'''

for t in range(int(input())):
    V, E = map(int, input().split())

    inf = float('inf')
    w_list = [[inf] * (V + 1) for _ in range(V + 1)]

    visit = [True] + [False] * V  # 최소신장트리는 시작을 임의 정점 -> 시작 노드를 0으로 둔다

    for _ in range(E):
        node1, node2, w = map(int, input().split())
        w_list[node1][node2] = w
        w_list[node2][node1] = w
        # 0 1 1
        # 1 0 6
        # 1 6 0

    cnt = 0  # V와 갯수비교!
    sum_w = 0  # 가중치 더하는 곳
    while cnt < V:
        min_w = 11  # 1 <= w <= 10
        for i in range(V + 1):
            if visit[i] == True:  # 내가 처음 visit을 설정할 때 0을 미리 True로 바꿔놨기 때문!!!
                for j in range(V + 1):
                    if visit[j] == False and min_w > w_list[i][j]:
                        min_w = w_list[i][j]
                        start_node = i
                        next_node = j

        visit[next_node] = True
        sum_w += w_list[start_node][next_node]
        cnt += 1

    print('#{} {}'.format(t+1, sum_w))

'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''