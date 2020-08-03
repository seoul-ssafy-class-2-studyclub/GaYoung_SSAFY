from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    check = deque()
    for j in range(bridge_length):
        check.append(0)
    trucks = deque()
    for i in range(len(truck_weights)):
        trucks.append(truck_weights[i])
    now_weight = 0
    while trucks:
        answer += 1
        x = check.popleft()  # 나갈것 내보내고
        now_weight -= x
        if trucks[0] + now_weight > weight:  # 못 들어가면
            check.append(0)
        else:  # 들어가면
            y = trucks.popleft()
            check.append(y)
            now_weight += y
    while len(check) != 0:
        answer += 1
        check.popleft()
    return answer