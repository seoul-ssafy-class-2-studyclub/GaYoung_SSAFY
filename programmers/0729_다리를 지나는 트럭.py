def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0] * bridge_length

    while truck_weights:
        answer += 1
        if truck_weights:
            q.pop(0)
            # print(q)
            # print(answer)
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
        print(q)

    return answer + 2

bridge_length=100
weight=100
truck_weights=[10]
print(solution(bridge_length, weight, truck_weights))