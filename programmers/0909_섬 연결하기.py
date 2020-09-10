n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def solution(n, costs):
    costs = sorted(costs, key=lambda x: x[2])
    visit = [0] * n
    total = 0
    visit[costs[0][0]] = 1
    while sum(visit) != n:
        print('1')
        for a, b, cost in costs:
            print('2')
            if visit[a] == 1 or visit[b] == 1:
                if visit[a] == 1 and visit[b] == 1:
                    print('3')
                    continue
                else:
                    visit[a] = 1
                    visit[b] = 1
                    total += cost  # 이게 가능한 이유는 costs를 cost 순으로 나열했기 때문
                    '''
                    [break 써야하는 이유]
                    break를 사용해야 for문이 끝나고 for문을 계속 새로 실행하면서 
                    if visit and visit에 걸려서 continue로 else문에 도착한다.
                    1 2 1 2 3 2 1 2 3 2 3 2
                    
                    break 사용하지 않으면 1 2 2 2 2 3 2 3 -> 모든 cost의 값들을 사용하지 못할 수 있음
                    '''
                    break  # break안하면 실패, 하면 통과

    return total


print(solution(n, costs))