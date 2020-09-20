board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

'''
1. bfs + 로봇은 2칸을 차지한다. + 회전
2. 방문 여부를 비교해야한다. -> 로봇의 좌표를 이용해야한다.
3. 회전함수 = turn -> 회전은 4가지 경우로 할 수 있다.
'''

'''
[문제점 : 시간초과]
1. 회전하는 함수를 이동하는 함수로 만들어버리기 
   -> while 안에서 for a, b in near:하고 회전함수 쓰면 5번인가부터 다 시간초과가 뜬다.
   -> move함수로 만들어버리면 13번만 시간초과가 뜬다

2. for res in move(location[0], location[1], bd):
   여기에서 if (len_board, len_board) in res: return cnt 이걸 먼저 확인해주고, 아니라면 visit, q에 넣는다.

3. [(),()] -> {(),()}로 바꿔준다. 이후 q에서 빼낼 때 {(),()} -> [(),()]로 바꿔준다
'''

'''
[다른 풀이법]
visit = board랑 똑같이 만든 다음에 상태를 나타낸다(가로인지, 세로인지)
'''


'''
[문제점 : index error]
1. turn 함수에서 result에 넣을 때, 회전했을 때의 결과를 넣어야한다!(헷깔리지 않게 조심!)
'''

from collections import deque

def move(first, second, bd):
    result = []
    dist = [1, -1]

    near = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for a, b in near:  # 이동
        # board의 값을 바꾸기에는 문제가 복잡해진다.
        # -> why? 로봇이 두칸을 차지하기때문에 first는 second로 가는 것이다.
        if bd[first[0] + a][first[1] + b] == 0 and bd[second[0] + a][second[1] + b] == 0:
            result.append({(first[0] + a, first[1] + b), (second[0] + a, second[1] + b)})

    if first[0] == second[0]:  # 가로 회전
        for d in dist:
            if bd[first[0]+d][first[1]] == 0 and bd[second[0]+d][second[1]] == 0:
                result.append({(first[0]+d, first[1]), (first[0], first[1])})
                result.append({(second[0] + d, second[1]), (second[0], second[1])})

    else:  # 세로 회전
        for d in dist:
            if bd[first[0]][first[1]+d] == 0 and bd[second[0]][second[1]+d] == 0:
                result.append({(first[0], first[1]), (first[0], first[1]+d)})
                result.append({(second[0], second[1]), (second[0], second[1]+d)})

    return result


def solution(board):

    len_board = len(board)
    bd = [[1] * (len_board + 2) for _ in range(len_board + 2)]
    for i in range(len_board):
        for j in range(len_board):
            bd[1+i][1+j] = board[i][j]


    q = deque([[[(1, 1), (1, 2)], 0]])
    visit = [[(1, 1), (1, 2)]]

    while q:

        location, cnt = q.popleft()
        location = list(location)

        for res in move(location[0], location[1], bd):
            if (len_board, len_board) in res:
                return cnt + 1

            if res not in visit:
                visit.append(res)
                q.append([res, cnt + 1])

print(solution(board))