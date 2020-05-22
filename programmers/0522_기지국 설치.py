import math

def solution(n, stations, w):
    distance = []
    cnt = 0  # 기지국 세우는 갯수
    for i in range(len(stations)):
        if i == 0:
            dist = stations[0] - w - 1
        else:
            dist = (stations[i] - w - 1) - (stations[i - 1] + w)
        distance.append(dist)

    # 기지국이 n의 마지막 숫자가 아닌경우
    if stations[-1] != n:
        dist = n - stations[-1] - w
        distance.append(dist)

    for i in distance:
        if i <= 0:
            continue
        else:
            cnt += math.ceil(i / (2 * w + 1))
        # elif i <= 2 * w + 1:
        #     cnt += 1
        # else:
        #     cnt += (i // (2 * w + 1) + 1)
    # print(cnt)

    return cnt

n = 11
stations = [4, 11]
w = 1

# n = 16
# stations = [9]
# w = 2

distance = []
cnt = 0  # 기지국 세우는 갯수
for i in range(len(stations)):
    if i == 0:
        dist = stations[0] - w - 1
    else:
        dist = (stations[i] - w - 1) - (stations[i - 1] + w)
    distance.append(dist)

# 기지국이 n의 마지막 숫자가 아닌경우
if stations[-1] != n:
    dist = n - stations[-1] - w
    distance.append(dist)
print(distance)
for i in distance:
    if i == 0:
        continue
    # elif i <= (2 * w + 1):
    #     cnt += 1
    else:
        cnt += math.ceil(i / (2 * w + 1))
print(cnt)