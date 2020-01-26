'''
[깊이 우선 탐색]
  1. 모든 경로 추적
  2. 경우의 수가 너무 많은 경우 처리 불가!
'''


'''
[백트래킹 기법]
  1. 어떤 노드에서 출발하는 경로가 해결책으로 이어지지 않을 것 같으면, 더이상 그 경로를 따라가지 않음
     -> 시도의 횟수 줄임
  2. 가지치기로 불필요한 경로 조기에 차단
  3. 백트래킹 알고리즘 적용으로 일반적으로 경우의 수가 줄어들어 처리 가능
     but, 최악의 경우 처리 불가능
  4. 유망성: 해답의 가능성이 있는 경우
  5. 가지치기 - 유망하지 않는 노드가 포함되는 경로는 더이상 고려하지 않음
'''


'''
[백트래킹을 이용한 알고리즘의 진행 절차]
  1. 상태 공간 트리에 대한 깊이 우선 탐색 실시
  2. 방문하는 노드가 유망한지 여부 점검
  3. 만일, 선택한 노드가 유망하지 않을 경우, 해당 노드의 부모노드로 돌아가서 검색 계속 진행
'''

'''
[일반적인 백트래킹 알고리즘]
def checknode(v):  # node : 현재 방문하는 node
    if promising(v):  # 현재 방문하는 node의 유망성을 판단
        if there is a solution at v:  # 유망하다면 함수 지속, 유망하지 않다면 stop
            write the solution
        else:
            for u in each child of v:  # 모든 자식 node를 방문하기 위해
                checknode(u)  # 재귀호출 실행
'''

'''
[상태 공간 트리]
방문하는 노드에서 해답을 찾을 가능성이 없는 경우 탐색 중지
'''

# [4-Queen 문제] : 대표적인 backtracking 문제
# 퀸이 놓이면, 다른 퀸이 놓일 수 없는 위치는 가로, 세로, 대각선, 역대각선 방향
# 1. 퀸을 한줄마다 놓을 때, 가로, 세로, 대각선에 위치한 퀸인지 확인
# 2. 맨 마지막이 될 때까지 모두 퀸을 놓을 수 있다면 cnt += 1
# 3. 모든 경우를 탐색하지만, 퀸을 놓을 수 없는자리라면 backtracking

def nqueen(ls, n):
    global cnt
    if n == len(ls):
        cnt += 1
        return 0
    s = [i for i in range(n)]
    for i in range(len(ls)):
        if ls[i] in s:
            s.remove(ls[i])
        check = len(ls) - i
        if ls[i] + check in s:
            s.remove(ls[i] + check)
        if ls[i] - check in s:
            s.remove(ls[i] - check)
    if s:
        for i in s:
            ls.append(i)
            nqueen(ls, n)
            ls.pop()


for t in range(int(input())):
    N = int(input())
    cnt = 0
    nqueen([], N)
    print('#{} {}'.format(t+1, cnt))