'''
3 2
1 2 1 2 1 2
'''

N, K = map(int, input().split())
A = list(map(int, input().split()))
robot = [0] * (N * 2)
answer = 0
while A.count(0) < K:

    # 1. 벨트가 한 칸 회전한다.
    A.insert(0, A.pop())
    robot.insert(0, robot.pop())
    robot[N - 1] = 0  # 로봇 bye~

    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
    # 만약 이동할 수 없다면 가만히 있는다.
    ls = []
    for i in range(N * 2 - 1, -1, -1):
        if robot[i] > 0:
            ls.append([robot[i], i])

    for r, idx in ls:
        if robot[idx + 1] == 0 and A[idx + 1] > 0:
            robot[idx] = 0
            robot[idx+1] = r
            A[idx+1] -= 1
    robot[N - 1] = 0  # 로봇 bye~

    if A[0] > 0:
        A[0] -= 1
        robot[0] = 1

    answer += 1

print(answer)
