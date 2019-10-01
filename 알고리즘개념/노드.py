''' 그래프'''
'''
풀이방식
1. 인접행렬 : 접근이 빠르지만 메모리 낭비 심함
2. 인접리스트: 접근이 느리지만 메모리 낭비 적음
         - V, E = 노드, 간선
         - adj = 인접리스트
'''


###### 무향그래프(=쌍방그래프) ######
''' [ 노드의 거리 ]
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내기
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6
 
 #1 2
'''

'''
[ 노드의 거리 풀이방법 ]
* 최소 길이 구하므로 bfs! *
1. 무향이므로 adj 쌍방으로 진행해야함
2-1. queue에서 -1(임의의 수)이 빠질 때, cnt += 1
3-1. -1은 매번 pop, append하는 것이 아니라, 한단계 나아가는 것을 모든 노드가 했을 때, -1을 넣어줌.
4-1. -1을 pop했는데, 또 pop할 때, -1을 하게되면, 그것은 길이 끊긴 것! -> break => cnt = 0(새로시작)

2-2. queue=[(start, cnt=0)]일 때, adj[node[0]]이 있고, visit에 그 해당 값이 없으면, 
     queue[[0][1]] += 1
3-2. while문 끝날때까지 반복!
'''
for t in range(int(input())):
    V, E = map(int, input().split())
    data = []
    for e in range(E):
        data.append(list(map(int, input().split())))
        # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    start, end = map(int, input().split())
    visit = []
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        adj[data[i][0]].append(data[i][1])
        adj[data[i][1]].append(data[i][0])

''' 방법1 '''
    cnt = 0
    queue = [start, -1]  # 연관 없는 숫자(-1)를 넣어서 -1이 나올 때마다 cnt += 1

    while queue:
        node = queue.pop(0)
        if node == end:
            break

        if node not in visit and node != -1:
            visit.append(node)
            queue.extend(adj[node])

        elif node == -1:
            queue.append(node)
            cnt += 1
            if queue[0] == -1:  # 이걸 하는 이유는?
                cnt = 0
                break

    print('#{} {}'.format(t + 1, cnt))

''' 방법2 '''
    queue = [(start, 0)]  # 이때, 0은 cnt

    while queue:
        node = queue.pop(0)
        rs = node[1]  # cnt를 print 하기위해
        if node[0] == end:
            result = rs
            break

        for r in adj[node[0]]:  # 1 -> 4, 3
            if r not in visit:
                visit.append(r)
            queue.append((r, rs + 1))

    print('#{} {}'.format(t + 1, result))


###### 유향그래프 ######
'''
[ 그래프경로 ]
경로가 존재하면 1, 없으면 0
1
6 5
1 4
1 3
2 3
2 5
4 6
1 6

#1 1
'''

'''
[ 그래프경로 풀이방법 ]
1. adj를 구한다.
2. 시작점부터 stack 또는 queue를 하면서 연결된 선으로 간다.
3. visit을 True로 바꾸거나, visit(빈 리스트)에 지나간 node값을 append한다.
4. 만약, 도착점이 visit안에 있거나, True가 되면 break한다.
'''
for t in range(int(input())):
    V, E = map(int, input().split())
    path = []
    for e in range(E):
        data = list(map(int, input().split()))
        path.append(data)
    start, end = map(int, input().split())
    visit = [False] * (V + 1)
    adj = [[] for _ in range(V + 1)]

    for p in path:
        adj[p[0]].append(p[1])  # [[], [4, 3], [3, 5], [], [6], [], []]

    result = 0
    stack = [start]
    visit[start] = True
    while stack:
        node = stack.pop()
        if visit[node] == False:
            visit[node] = True
            if visit[end]:
                result = 1
                break
        stack.extend(adj[node])
    print('#{} {}'.format(t + 1, result))



'''
[ 작업순서 ]
특정 작업이 끝나야 시작할 수 있으며, 이를 선행 관계라 하자. 이런 작업의 선행 관계를 나타낸 그래프가 주어진다.
한 사람이 한 번에 하나씩 일을 할 수 있는 작업 순서를 찾는 프로그램을 작성하라.
ex. 9 9
    4 1 1 2 2 3 2 7 5 6 7 6 1 5 8 5 8 9
    Ans. #1 8 9 4 1 5 2 3 7 6
'''

'''
[ 작업순서 풀이방법 ]
1. adj를 만든다.
2. 하나의 노드에 여러 간선이 닿을 수 있으므로 visit을 [None]+[0]*v라고 설정하고 visit에 더해줌
3. visit[node] == 0이 되면 다른 숫자 또는 문자로 수정 -> 작업 끝
4. 0이 될 때, stack에 넣음
'''
for t in range(int(input())):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))
    adj = [[] for i in range(V + 1)]
    visit = [None] + [0] * V

    for i in range(0, len(data), 2):
        adj[data[i]].append(data[i + 1])
        visit[data[i + 1]] += 1

    stack = []
    result = ''
    for i in range(1, V + 1):
        stack.append(i)
        while stack:
            node = stack.pop()
            if visit[node] > 0:
                visit[node] -= 1
            elif visit[node] == 0:
                visit[node] = 'X'
                result += str(node) + ' '
                stack.extend(adj[node])

    print('#{} {}'.format(t + 1, result))
