# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

bridge_length = 100
weight = 100
truck_weights = [10]

def solution(bridge_length, weight, truck_weights):

    bridge = [0] * bridge_length

    time = 0
    while truck_weights:
        time += 1

        bridge.pop(0)  # if, else 둘다 필요하다.

        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))

        else:
            bridge.append(0)

    return time + bridge_length