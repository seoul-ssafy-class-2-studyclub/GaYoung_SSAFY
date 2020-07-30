def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length  # [0, 0]

    while truck_weights:
        answer += 1
        q.pop(0)
        print(q)
        print(answer)
        if sum(q) + truck_weights[0] <= weight:
            q.append(truck_weights.pop(0))
        else:
            q.append(0)

    return answer