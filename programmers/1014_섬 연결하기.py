# n = 4
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# n = 5
# costs = [[0, 1, 1], [3, 1, 1], [0, 2, 2], [0, 3, 2], [0, 4, 100]]

# n = 5
# costs = [[0,1,5],[1,2,3],[2,3,3],[3,1,2],[3,0,4],[2,4,6],[4,0,7]]

# n = 5
# costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,3],[2,3,8],[3,4,1]]

n = 4
costs = [[0,1,1],[0,2,2],[2,3,1]]

def solution(n, costs):

    costs = sorted(costs, key=lambda x:x[2])
    visit = [0] * n
    visit[costs[0][0]] = 1
    total = 0
    while True:
        if sum(visit) == n:
            print('total')
            return total

        for start, end, cost in costs:
            print('start')
            if visit[start] == 1 or visit[end] == 1:
                print('1')
                if visit[start] == 1 and visit[end] == 1:
                    print('2')
                    continue
                else:
                    print('3')
                    visit[start] = 1
                    visit[end] = 1
                    total += cost
                    # print('break')
                    break  # break가 있어야 중복확인 없이 바로 다음 값으로 넘어간다.
                           # break O : [0,1,1]다음에 [0,2,2]다음에 [2,3,1] 확인
                           # break X : [0,1,1]다음에 [0,1,1], [0,2,2]다음에 [0,1,1], [0,2,2], [2,3,1] 확인


print(solution(n, costs))

