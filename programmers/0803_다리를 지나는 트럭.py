def solution(bridge_length, weight, truck_weights):
    answer = 0
    return answer


bridge_length=2
weight=10
truck_weights=[7,4,5,6]

answer = 0
check = [0] * bridge_length

while truck_weights:
    answer += 1
    x = check.pop(0)
    if truck_weights[0] + x + sum(check) > weight:
        check.append(0)
    else:
        y = truck_weights.pop(0)
        check.append(y)

    # print(check)

    while len(check) == 0:
        answer += 1
        check.pop(0)

    # print(answer)



