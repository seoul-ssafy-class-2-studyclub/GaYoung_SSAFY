def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length

    time = 0
    while truck_weights:
        time += 1

        bridge.pop(0)

        if (sum(bridge) + truck_weights[0]) <= weight:
            x = truck_weights.pop(0)
            bridge.append(x)
        else:
            bridge.append(0)

    return time + bridge_length


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

# bridge_length = 100
# weight = 100
# truck_weights = [10,10,10,10,10,10,10,10,10,10]

